# Tool Documentation

This file serves as documentation for the tools in the python toolbox. The metadata for each individual tool has been populated, and these same documentation concepts are accessible in the tool tips for each tool. Though efforts will be made to ensure both sets are synchronized, this page will represent the most up-to-date documentation for the individual tools.

## Evaluate Extremes Across Table

Evaluates each record in a table across a defined set of columns to find the highest or lowest values. These results are written to three new fields in either the input dataset or a new output file. The three new fields describe, for each row, the highest or lowest value in the evaluation, the name of the field that contained that value, and whether there was a tie between the winning field and another field.

### Parameters

Many of the parameters in this tool are auto-populated by smart validation procedures but can be modified if desired prior to running.

Parameter | Description
-----------| -----------
Input Feature Class or Table | The input layer or table containing the values to be evaluated. Feature Classes, Geodatabase Tables, and CSV files are supported as input. Note that when using a CSV file, you must write the results to a new file. You will not have the option of writing the output values directly to the input table.
Fields to Evaluate | The fields in the input dataset to evaluate. The fields must be numeric (Short, Long, Float, and Double), but don't all have to be of the same format. When using a mix of formats in the input, the output value field will use the most complex field type represented in the data. Short < Long < Float < Double.
Evaluation Type | The evaluation type that will be used to define the winning field and value.<br><br><ul><li>Highest Value - returns the highest discovered value and respective field name per row.</li><li>Lowest Value - returns the lowest discovered value and respective field name per row.</li></ul>
Tiebreaker Handing | Determines how the tool handles situations in which multiple columns have the discovered Highest/Lowest value.<br><br><ul><li>First - returns the first column with the discovered Highest/Lowest value.</li><li>Last - returns the last column with the discovered Highest/Lowest value.</li></ul>
Winning Field Name | The tool creates a new field who's value will be the name of the field that has the winning value. This will be the *name* of that new field.
Winning Field Alias | The tool creates a new field who's value will be the name of the field that contained the winning value. This will be the *alias* of that new field.
Winning Field Value | The newly created Winning Field will contain the name of the field that originally contained the winning values. There are two options for how this value is populated.<br><br><ul><li>Use Winning Field's Alias - The winning field's alias (instead of name) will be used as the value.</li><li>Use Winning Field's Name - The winning field's name (instead of alias) will be used as the value.</li></ul>
Winning Value Name | The tool creates a new field that contains the winning value. This will be the name of that new field.
Winning Value Alias | The tool creates a new field that contains the winning value. This will be the alias of that new field.
Tie Detection Name | A field is created to document the detection of a tie for the Highest/Lowest values. This is the *name* of that output field.
Tie Detection Alias | A field is created to document the detection of a tie for the Highest/Lowest values. This is the *alias* of that output field.
Output Type | Describes where the output will be created. This parameter will be disabled and default to "Create Copy" if the input is not a geodatabase item.<br><br><ul><li>Modify Input - New fields and results will be written directly to the input layer.</li><li>Create Copy - Input will be copied and new fields and results will be written to the copy.</li></ul>
Output File | If Output Type is set to Create Copy, the output will be written to the specified location.



## Rank Values Across Table

Evaluates each record in a table across a defined set of columns to rank the **n** top or bottom values. These results are written to a number of new fields in either the input dataset or a new output file. The number of new output fields is dependent on the number of ranks specified. Each rank will create two new fields. For example if 3 ranks are desired, 6 new fields will be created. The two new fields per rank describe, for each row, the name of the field containing the ranked value, and the ranked value itself.

## Parameters

Many of the parameters in this tool are auto-populated by smart validation procedures but can be modified if desired prior to running.

Parameter | Description
-----------| -----------
Input Feature Class or Table | The input layer or table containing the values to be evaluated. Feature Classes, Geodatabase Tables, and CSV files are supported as input. Note that when using a CSV file, you must write the results to a new file. You will not have the option of writing the output values directly to the input table.
Fields to Evaluate | The fields in the input dataset to evaluate. The fields must be numeric (Short, Long, Float, and Double), but don't all have to be of the same format. When using a mix of formats in the input, the output value field will use the most complex field type represented in the data. Short < Long < Float < Double
Ranking Type | The ranking type that will be used to define the winning field and value.<br><br><ul><li>Top - returns the highest x values and their respective field names across the row.</li><li>Bottom - returns the lowest x values and their respective field names across the row.</li></ul>
Ranks | The number of ranks to evaluate and create. Keep in mind that each rank will create two new fields in the output.
Output Type | Describes where the output will be created. This parameter will be disabled and default to "Create Copy" if the input is not a geodatabase item.<br><br><ul><li>Modify Input - New fields and results will be written directly to the input layer.</li><li>Create Copy - Input will be copied and new fields and results will be written to the copy.</li></ul>
Output File | If Output Type is set to Create Copy, the output will be written to the specified location.
Style for Output Rank Fields | The newly created Winning Field will contain the name of the field that originally contained the winning values. There are two options for how this value is populated.<br><br><ul><li>Use Field's Alias - The winning field's alias (instead of name) will be used as the value.</li><li>Use Field's Name - The winning field's name (instead of alias) will be used as the value.</li></ul>
Rank Prefix | The names of the new fields written the output will be based on the following schema: [rankPrefix][rank]_Field and [rankPrefix][rank]_Value (e.g r1_Field and r1_Value). If this default schema conflicts with existing fields in the schema, the prefix can be changed to something unique.
