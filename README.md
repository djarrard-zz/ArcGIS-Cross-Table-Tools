# ArcGIS Cross-Table Tools

## Features
 
This project is intended as an immediately usable resource in the ArcGIS Pro environment that allows users to evaluate values across a table, per row. Though these functions are achievable through a series of field calculations using out-of-the-box tools, it would take a high amount of effort and precision to build those expressions. The individual tools in this python toolbox allow for an expedient, code-free process to evaluate values across a table.

* Evaluate Extremes Across Table - Evaluates each record in a table across a defined set of columns to find the highest or lowest values. These results are written to three new fields in either the input dataset or a new output file. The three new fields describe, for each row, the highest or lowest value in the evaluation, the name of the field that contained that value, and whether there was a tie between the winning field and another field.

* Rank Values Across Table - Evaluates each record in a table across a defined set of columns to rank the **n** top or bottom values. These results are written to a number of new fields in either the input dataset or a new output file. The number of new output fields is dependent on the number of ranks specified. Each rank will create two new fields. For example if 3 ranks are desired, 6 new fields will be created. The two new fields per rank describe, for each row, the name of the field containing the ranked value, and the ranked value itself.
 
 ## Instructions and Notes
 
 1. Download the repository ZIP file.
 2. Extract the ZIP file to the desired folder.
 3. If necessary, in your ArcGIS Pro project, use the Catalog view to add a connection to the folder containing the extracted repository.
 4. In the Catalog view, expand the Table Tools.pyt toolbox.
 5. Double-Click on the desired tool.
 
 The documentation for each tool is built-in to the metadata. For each field the "i" button will provide guidance on proper usage.
 
 ## Requirements
 
 1. ArcGIS Pro 2.3.2 or higher. Lower versions may work but have not been tested.
 2. The Geoprocessing tools used in the toolbox only require a Basic license (Standard and Advanced are of course supported, but not required).
 
 ## Issues
 
If there are bugs/issues with the tool that prevent usage or create incorrect results, please let me know by submitting an issue. I am also open to expanding the toolbox to include other use cases that require cross-table examination in a similar fashion. Please feel free to submit enhancement requests along those lines.

## Licensing

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at


   http://www.apache.org/licenses/LICENSE-2.0


Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


A copy of the license is available in the repository.

