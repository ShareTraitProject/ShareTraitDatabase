# question-query for master-query view

## Question

**master-query**

Generate a query to provide as output the complete sharetrait version 1.0.0 published in a csv version. 
## Query

Name : master-query.sql
Description: 

## Comments

- In terms of values, in particular to measurements and trait characteristics, this query completes all information with complete association as found in the original dataset.
- However, there is some extensions of information and this is based on testing the database. For example, sharetrait dataset does not contain taxonomy information. Or better, the only information that it contains deals with the attribute "species_reported".
- However, as we designed and implemented the Taxonomy category, taking into account the existence of reference names, indipendendly of the source (tree of life, catalogue of life, ncbi..), we have included some parameters to test the functions. Such as adding a genus name for testing aggregations based on group of species. Ideally, someone will need to make sure that the reference namings and hierarchies are included.
- Another difference which is not making the output incorrect but just using a different term is for the Method category in which there is metadata dealing with the condition and circumstances the measurement was collected/obtained.
- In this case, because different situations do contain the same type of metadata (e.g. temperature, humidity for instance), we designed the condition to contain a type field (such as experiment, maintenance...). For this reason, the attribute of sharetrait dataset
- Due to the design and implementation 
