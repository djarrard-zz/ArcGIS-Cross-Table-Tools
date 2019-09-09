# -*- coding: utf-8 -*-

import arcpy, time


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Table Tools"
        self.alias = "TableTools"

        # List of tool classes associated with this toolbox
        self.tools = [evalExtremes, rankAcross]


class evalExtremes(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Evaluate Extremes Across Table"
        self.description = "Compares values in multiple fields and identifies a 'winning value' based on input criteria"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""

        #param0 logic
        param0 = arcpy.Parameter(
            displayName = "Input Feature Class or Table",
            name = "inputLayer",
            datatype = ["DEFeatureClass","GPFeatureLayer","DETable","DEDbaseTable","GPTableView","DETextfile"],
            parameterType = "Required",
            direction = "Input")

        #param1 logic
        param1 = arcpy.Parameter(
            displayName = "Fields To Evaluate",
            name = "fields",
            datatype = "Field",
            parameterType = "Required",
            direction = "Input",
            multiValue = True)

        param1.parameterDependencies = [param0.name]
        param1.filter.list = ["Short","Long","Float","Double"]

        #param2 logic
        param2 = arcpy.Parameter(
            displayName = "Evaluation Type",
            name = "evalType",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input")

        param2.filter.type = "ValueList"
        param2.filter.list = ["Highest Value","Lowest Value"]
        param2.value = "Highest Value"

        #param3 logic
        param3 = arcpy.Parameter(
            displayName = "Tiebreaker Handling",
            name = "tieBreakerHandling",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input")

        param3.filter.type = "ValueList"
        param3.filter.list = ["First","Last"]
        param3.value = "First"

        #param4 logic
        param4 = arcpy.Parameter(
            displayName = "Name",
            name = "winningFieldName",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input",
            category = "Output Field: Winning Field")

        param4.value = "Highest_Field"

        #param5 logic
        param5 = arcpy.Parameter(
            displayName = "Alias",
            name = "winningFieldAlias",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input",
            category = "Output Field: Winning Field")

        param5.value = "Highest Field"

        #param6 logic
        param6 = arcpy.Parameter(
            displayName = "Value",
            name = "winningFieldValue",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input",
            category = "Output Field: Winning Field")

        param6.filter.type = "ValueList"
        param6.filter.list = ["Use Winning Field's Name","Use Winning Field's Alias"]
        param6.value = "Use Winning Field's Name"

        #param7 logic
        param7 = arcpy.Parameter(
            displayName = "Name",
            name = "winningValueName",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input",
            category = "Output Field: Winning Value")

        param7.value = "Highest_Value"

        #param8 logic
        param8 = arcpy.Parameter(
            displayName = "Name",
            name = "winningValueAlias",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input",
            category = "Output Field: Winning Value")

        param8.value = "Highest Value"

        #param9 logic
        param9 = arcpy.Parameter(
            displayName = "Name",
            name = "tieDetectionName",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input",
            category = "Output Field: Tie Detection")

        param9.value = "Tie_Detected"

        #param10 logic
        param10 = arcpy.Parameter(
            displayName = "Name",
            name = "tieDetectionAlias",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input",
            category = "Output Field: Tie Detection")

        param10.value = "Tie Detected"

        #param11 logic
        param11 = arcpy.Parameter(
            displayName = "Output Type",
            name = "outputType",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input")

        param11.filter.type = "ValueList"
        param11.filter.list = ["Modify Input", "Create Copy"]
        param11.value = "Modify Input"

        #param12 logic
        param12 = arcpy.Parameter(
            displayName = "Output File",
            name = "outputFile",
            datatype = ["DEFeatureClass","DETable"],
            parameterType = "Optional",
            direction = "Output")

        params = [param0,param1,param2,param3,param4,param5,param6,param7,param8,param9,param10,param11,param12]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""

        if parameters[0].altered:
            gdbItemTypes = ["TableView","Table","FeatureClass","FeatureLayer"]
            input = arcpy.Describe(parameters[0].value)
            if input.datatype not in gdbItemTypes:
                parameters[11].value = "Create Copy"
                parameters[11].enabled = 0
            else:
                parameters[11].enabled = 1
        if parameters[2].value == "Highest Value":
            if parameters[4].value == "Lowest_Field":
                parameters[4].value = "Highest_Field"
            if parameters[5].value == "Lowest Field":
                parameters[5].value = "Highest Field"
            if parameters[7].value == "Lowest_Value":
                parameters[7].value = "Highest_Value"
            if parameters[8].value == "Lowest Value":
                parameters[8].value = "Highest Value"
        elif parameters[2].value == "Lowest Value":
            if parameters[4].value == "Highest_Field":
                parameters[4].value = "Lowest_Field"
            if parameters[5].value == "Highest Field":
                parameters[5].value = "Lowest Field"
            if parameters[7].value == "Highest_Value":
                parameters[7].value = "Lowest_Value"
            if parameters[8].value == "Highest Value":
                parameters[8].value = "Lowest Value"
        if parameters[11].value == "Create Copy":
            parameters[12].enabled = 1
        if parameters[11].value == "Modify Input":
            parameters[12].enabled = 0

        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        if parameters[0].altered:
            gdbItemTypes = ["TableView","Table","FeatureClass","FeatureLayer"]
            input = arcpy.Describe(parameters[0].value)
            if input.datatype not in gdbItemTypes:
                parameters[0].setWarningMessage("Specified input is read-only and can't be modified. Results must be written as a new geodatabase table. The option to write results back to input table have been disabled.")
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        import pandas

        #Get input parameters from tool
        inFile = parameters[0].valueAsText
        inFields = parameters[1].valueAsText
        evalType = parameters[2].valueAsText
        tieBreaker = parameters[3].valueAsText
        wFN = parameters[4].valueAsText
        wFA = parameters[5].valueAsText
        wFV = parameters[6].valueAsText
        wVN = parameters[7].valueAsText
        wVA = parameters[8].valueAsText
        tieField = parameters[9].valueAsText
        tieAlias = parameters[10].valueAsText
        outType = parameters[11].valueAsText
        outFile = parameters[12].valueAsText

        #Evaluate whether to modify input or create a copy
        if outType == "Create Copy":
            messages.addMessage("Creating copy of input to {0}".format(outFile))
            desc = arcpy.Describe(inFile)
            if desc.datatype in ["FeatureLayer", "FeatureClass"]:
                arcpy.CopyFeatures_management(inFile, outFile)
            else:
                arcpy.CopyRows_management(inFile, outFile)
            processInput = outFile
        else:
            messages.addMessage("Updates will be written to input layer.")
            processInput = inFile

        #Evaluate field types in input to determine output field types
        fieldList = inFields.split(";")
        fieldDict = {}
        fieldTypes = []
        fieldsObject = arcpy.ListFields(inFile)
        for field in fieldsObject:
            if field.name in fieldList:
                fieldDict[field.name]=[field.name,field.aliasName,field.type]
        for entry in fieldDict:
            fType = fieldDict[entry][2]
            if fType not in fieldTypes:
                fieldTypes.append(fType)
        if len(fieldTypes) > 1:
            if "Double" in fieldTypes:
                messages.addMessage("Multiple numeric field types detected. Most complex type is Double, therefore Double format will be used in the output.")
                outFieldType = "Double"
            elif "Float" in fieldTypes:
                messages.addMessage("Multiple numeric field types detected. Most complex type is Float, therefore Float format will be used in the output.")
                outFieldType = "Float"
            elif "Long" in fieldTypes:
                messages.addMessage("Multiple numeric field types detected. Most complex type is Long, therefore Long format will be used in the output.")
                outFieldType = "Long"
        else:
            messages.addMessage("Single numeric field ({0} type) for all selected evaluation fields. Output fields will therefore be type {1}".format(fieldTypes[0],fieldTypes[0]))
            outFieldType = fieldTypes[0]
        evalFieldCount = len(fieldList)

        #Add new fields to input
        arcpy.AddField_management(processInput,wFN,"TEXT","","","50",wFA)
        fieldList.append(wFN)
        arcpy.AddField_management(processInput,wVN,outFieldType,"","","",wVA)
        fieldList.append(wVN)
        arcpy.AddField_management(processInput,tieField,"TEXT","","","3",tieAlias)
        fieldList.append(tieField)
        messages.addMessage("Added fields {0}, {1}, and {2} to feature class.".format(wFN,wVN,tieField))

        #Evaluate values and write results
        countObject = arcpy.GetCount_management(inFile)
        count = int(countObject[0])
        arcpy.SetProgressor("Step","Evaluating column values...",1,count,1)
        with arcpy.da.UpdateCursor(processInput,fieldList) as uCursor:
            warnings = 0
            r = 1
            for row in uCursor:
                arcpy.SetProgressorLabel("Processing {0} of {1} features".format(r,count))
                i = 0
                evalData = {}
                while i <= evalFieldCount - 1:
                    field = fieldList[i]
                    val = row[i]
                    evalData[field]=val
                    i += 1
                s = pandas.Series(evalData)

                if evalType == "Highest Value":
                    if s.nlargest(2)[0] == s.nlargest(2)[1]:
                        tieDetect = "Yes"
                    else:
                        tieDetect = "No"
                    winValue = s.nlargest(1,keep=tieBreaker.lower())[0]
                    if wFV == "Use Winning Field's Alias":
                        winField = fieldDict[s.nlargest(1,keep=tieBreaker.lower()).index[0]][1]
                    else:
                        winField = s.nlargest(1,keep=tieBreaker.lower()).index[0]
                else:
                    if s.nsmallest(2)[0] == s.nsmallest(2)[1]:
                        tieDetect = "Yes"
                    else:
                        tieDetect = "No"
                    winValue = s.nsmallest(1,keep=tieBreaker.lower())[0]
                    if wFV == "Use Winning Field's Alias":
                        winField = fieldDict[s.nsmallest(1,keep=tieBreaker.lower()).index[0]][1]
                    else:
                        winField = s.nsmallest(1,keep=tieBreaker.lower()).index[0]
                row[i]=winField
                if outFieldType == "Double":
                    row[i+1] = float(winValue)
                else:
                    row[i+1] = int(winValue)
                row[i+2] = tieDetect
                uCursor.updateRow(row)
                arcpy.SetProgressorPosition()
                r += 1


        return


class rankAcross(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Rank Values Across Table"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        #param0 logic
        param0 = arcpy.Parameter(
            displayName = "Input Feature Class or Table",
            name = "inputLayer",
            datatype = ["DEFeatureClass","GPFeatureLayer","DETable","DEDbaseTable","GPTableView","DETextfile"],
            parameterType = "Required",
            direction = "Input")

        #param1 logic
        param1 = arcpy.Parameter(
            displayName = "Fields To Evaluate",
            name = "fields",
            datatype = "Field",
            parameterType = "Required",
            direction = "Input",
            multiValue = True)

        param1.parameterDependencies = [param0.name]
        param1.filter.list = ["Short","Long","Float","Double"]

        #param2 logic
        param2 = arcpy.Parameter(
            displayName = "Ranking Type",
            name = "evalType",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input")

        param2.filter.type = "ValueList"
        param2.filter.list = ["Top","Bottom"]
        param2.value = "Top"

        #param3 logic
        param3 = arcpy.Parameter(
            displayName = "Ranks",
            name = "ranks",
            datatype = "GPLong",
            parameterType = "Required",
            direction = "Input")

        #param4 logic
        param4 = arcpy.Parameter(
            displayName = "Output Type",
            name = "outputType",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input")

        param4.filter.type = "ValueList"
        param4.filter.list = ["Modify Input", "Create Copy"]
        param4.value = "Modify Input"

        #param5 logic
        param5 = arcpy.Parameter(
            displayName = "Output File",
            name = "outputFile",
            datatype = ["DEFeatureClass","DETable"],
            parameterType = "Optional",
            direction = "Output")

        #param6 logic
        param6 = arcpy.Parameter(
            displayName = "Style for Output Rank Fields",
            name = "fieldStyle",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input",
            category = "Output Fields Configuration")

        param6.filter.type = "ValueList"
        param6.filter.list = ["Use Field's Name","Use Field's Alias"]
        param6.value = "Use Field's Name"

        #param7 logic
        param7 = arcpy.Parameter(
            displayName = "Rank Prefix",
            name = "rankPrefix",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input",
            category = "Output Fields Configuration")

        param7.value = "r"

        params = [param0,param1,param2,param3,param4,param5,param6,param7]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""

        if parameters[0].altered:
            gdbItemTypes = ["TableView","Table","FeatureClass","FeatureLayer"]
            input = arcpy.Describe(parameters[0].value)
            if input.datatype not in gdbItemTypes:
                parameters[4].value = "Create Copy"
                parameters[4].enabled = 0
            else:
                parameters[4].enabled = 1

        if parameters[4].value == "Create Copy":
            parameters[5].enabled = 1
        if parameters[4].value == "Modify Input":
            parameters[5].enabled = 0

        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        if parameters[1].altered and parameters[3].altered:
            fields = str(parameters[1].value)
            fieldCount = len(fields.split(";"))
            if fieldCount < parameters[3].value:
                parameters[3].setErrorMessage("Rank value can't exceed number of input fields")

        if parameters[0].altered:
            gdbItemTypes = ["TableView","Table","FeatureClass","FeatureLayer"]
            input = arcpy.Describe(parameters[0].value)
            if input.datatype not in gdbItemTypes:
                parameters[0].setWarningMessage("Specified input is read-only and can't be modified. Results must be written as a new geodatabase table. The option to write results back to input table have been disabled.")

        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        import pandas

        #Get input parameters from tool
        inFile = parameters[0].valueAsText
        inFields = parameters[1].valueAsText
        rankType = parameters[2].valueAsText
        ranks = int(parameters[3].valueAsText)
        outType = parameters[4].valueAsText
        outFile = parameters[5].valueAsText
        fieldStyle = parameters[6].valueAsText
        prefix = parameters[7].valueAsText

        #Evaluate whether to modify input or create a copy
        if outType == "Create Copy":
            messages.addMessage("Creating copy of input to {0}".format(outFile))
            desc = arcpy.Describe(inFile)
            if desc.datatype in ["FeatureLayer", "FeatureClass"]:
                arcpy.CopyFeatures_management(inFile, outFile)
            else:
                arcpy.CopyRows_management(inFile, outFile)
            processInput = outFile
        else:
            messages.addMessage("Updates will be written to input layer.")
            processInput = inFile

        #Evaluate field types in input to determine output field types
        fieldList = inFields.split(";")
        fieldDict = {}
        fieldTypes = []
        fieldsObject = arcpy.ListFields(inFile)
        for field in fieldsObject:
            if field.name in fieldList:
                fieldDict[field.name]=[field.name,field.aliasName,field.type]
        for entry in fieldDict:
            fType = fieldDict[entry][2]
            if fType not in fieldTypes:
                fieldTypes.append(fType)
        if len(fieldTypes) > 1:
            if "Double" in fieldTypes:
                messages.addMessage("Multiple numeric field types detected. Most complex type is Double, therefore Double format will be used in the output.")
                outFieldType = "Double"
            elif "Float" in fieldTypes:
                messages.addMessage("Multiple numeric field types detected. Most complex type is Float, therefore Float format will be used in the output.")
                outFieldType = "Float"
            elif "Long" in fieldTypes:
                messages.addMessage("Multiple numeric field types detected. Most complex type is Long, therefore Long format will be used in the output.")
                outFieldType = "Long"
        else:
            messages.addMessage("Single numeric field type ({0}) for all selected evaluation fields. Output fields will therefore be type {1}".format(fieldTypes[0],fieldTypes[0]))
            outFieldType = fieldTypes[0]
        evalFieldCount = len(fieldList)

        #Add new fields to input
        i = 1
        while i <= ranks:

            fieldName = "{0}{1}_Field".format(prefix,i)
            arcpy.AddField_management(processInput,fieldName,"TEXT","","","50",fieldName)
            messages.addMessage("Added {0} field to output...".format(fieldName))
            fieldList.append(fieldName)

            valName = "{0}{1}_Value".format(prefix,i)
            arcpy.AddField_management(processInput,valName,outFieldType,"","","",valName)
            messages.addMessage("Added {0} field to output...".format(valName))
            fieldList.append(valName)

            i += 1

        #Evaluate values and write results
        countObject = arcpy.GetCount_management(inFile)
        count = int(countObject[0])
        arcpy.SetProgressor("Step","Evaluating column values...",1,count,1)

        with arcpy.da.UpdateCursor(processInput,fieldList) as uCursor:
            base = len(inFields.split(";"))
            warnings = 0
            r = 1
            for row in uCursor:
                base = len(inFields.split(";"))
                arcpy.SetProgressorLabel("Processing {0} of {1} features".format(r,count))
                i = 0
                evalData = {}
                while i <= evalFieldCount - 1:
                    field = fieldList[i]
                    val = row[i]
                    evalData[field]=val
                    i += 1

                s = pandas.Series(evalData)
                if rankType == "Top":
                    rankResults = s.nlargest(ranks)
                else:
                    rankResults = s.nsmallest(ranks)
                for n in range(ranks):
                    rankVal = rankResults[n]
                    if fieldStyle == "Use Field's Alias":
                        winField = fieldDict[rankResults.index[n]][1]
                    else:
                        winField = rankResults.index[n]
                    row[base + n] = winField
                    row[base + n + 1] = rankVal
                    base += 1
                uCursor.updateRow(row)
                arcpy.SetProgressorPosition()

        return
