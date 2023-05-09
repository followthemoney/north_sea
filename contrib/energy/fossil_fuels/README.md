# Fossil Fuel Extraction

## Data

All data can be found [here](https://drive.google.com/drive/folders/1XL40_KcAIXIFhjfFzeLE1tPU_8OZlq5M?usp=sharing). 

### Oil and Gas production sources

* Netherlands: [NLOGS](https://nlog.nl)
* Netherlands: [Mijnbouwvergunningen](https://mijnbouwvergunningen.nl/)
* United Kingdom: [North Sea Transition Authority](https://www.nstauthority.co.uk/)
* Denmark: [Danish Energy Agency](https://ens.dk/en/our-responsibilities/oil-gas)
* Norway: [Norsk Petroleum](https://www.norskpetroleum.no/)
* Norway: [Petroleum Register](https://www.npd.no/en/regulations/reporting_and_applications/petroleum-register/)
* Iceland: [National Energy Authority](https://nea.is/)
* Europe: [EMODnet Active Licenses](https://www.emodnet-humanactivities.eu/search-results.php?dataname=Active+Licences)

### Data considerations

#### Units

There are several units to measure gas volume and prices, for instance:
- standard cubic meter (Sm3). 
- normal cubic meter (Nm3)
- million British Thermal Units ([MMBtu](https://nl.wikipedia.org/wiki/British_thermal_unit))
- kWh/MWh
- [Barrel](https://en.wikipedia.org/wiki/Barrel_(unit))

TL;DR: it's hard to measure exact volumes of oil and gas, but generally most production statistics are measured in Sm3.

Some resources for measurement units and conversion:
- [BP](https://www.bp.com/content/dam/bp/business-sites/en/global/corporate/pdfs/energy-economics/statistical-review/bp-stats-review-2021-approximate-conversion-factors.pdf)
- [UNSTATS](https://unstats.un.org/oslogroup/meetings/og-04/docs/oslo-group-meeting-04--escm-ch04-draft2.pdf)


#### Normalization

Companies are active in multiple North Sea countries, often under different names. For instance Wintershall Noordzee B.V., Wintershall DEA, Wintershall A/S. These names need to be normalized by adding relationships between these companies, so we can aggregate it to the main company entity. These relationships also need to be established over time, to capture mergers, joint ventures, name changes, etc. This is a lot of (manual) work.

### Important entities

1. License: A licence is required to engage in any exploration for or production of mineral resources or geothermal energy and for the storage of substances. . Additional permits are also required for activities such as drilling a well at a particular location or constructing a production facility. Both onshore and offshore, the same area may be covered by both a ’shallow’ and a ‘deep’ licence ([source](https://www.nlog.nl/en/licences))

2. Operator: Oil and gas operator means any person or persons, firm, partnership, partnership association or corporation that proposes to or does locate, drill, operate or abandon any oil or gas well or engaged in the operation of pipeline facilities or the transportation of oil or gas. ([source](https://www.lawinsider.com/dictionary/oil-and-gas-operator))

3. Licensee: The companies that own the license. Sometimes the operator owns the license, but often other companies are involved, or the operator doens't have a share. One license can have multiple licensees. In most countries the shares are specified, but not in the Netherlands.

4. Block: a spatial grid of the continental shelf which are part of a license area. For instance, this is how it works in the UK. "The UKCS (United Kingdom Continental Shelf) is divided into quadrants of 1 degree latitude and one degree longitude. Each quadrant is divided into 30 blocks measuring 10 minutes of latitude and 12 minutes of longitude. Some blocks are divided further into part blocks where some areas are relinquished by previous licensees. For example, block 13/24a is located in quad 13 and is the 24th block and is the 'a' part block. The UK government has traditionally issued licences via periodic (now annual) licensing rounds. Blocks are awarded on the basis of the work programme bid by the participants. The UK government has actively solicited new entrants to the UKCS via "promote" licensing rounds with less demanding terms and the fallow acreage initiative, where non-active licences have to be relinquished" ([source](https://en.wikipedia.org/wiki/Petroleum_licensing))

5. Well / Field / Reservoir: On Quora [this consultant](https://www.quora.com/What-is-the-difference-between-an-oil-field-an-oil-well-and-an-oil-reservoir/answer/Phil-Knight-23) has a clear answer to what the difference is. "An oil well is basically a hole in the ground that pierces an oil reservoir. An oil reservoir is a geological structure that contains hydrocarbon classically in a porous sandstone structure (other geological structures can and do contain oil, this is just an example).An oil field is a number of oil wells intersecting an oil reservoir" 

6. Authority: Each country has an authority that is responsible for granting licenses. There is a difference though between granting the licenses and reporting on them. In the Netherlands, for instance, the Ministry of Economic Affairs grants licenses, but NLOG report on them, while Staatstoezicht op de Mijnen advises the Ministry.

### Spatial data

All authorities provide spatial data sets of oil fields, wells, blocks, licenses and licensees. See the data sources above. 


