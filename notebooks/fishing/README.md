# Fishing effort in the Northsea

The goal of these notebooks is to assess the fishing efforts in the North Sea in the last ten years (2012-2022). The data and methods of [Global Fishing Watch](https://globalfishingwatch.org/) are used. The API documentation can be [found here](https://globalfishingwatch.org/our-apis/documentation#introduction)

Jupyter Notebooks are used to explore the different API endpoints of Global Fishing Watch. 

Some important steps are:
1. Aggregate fishing efforts in grid cells in Marine Protected Areas
2. Group by vessel_id, year and gear.
3. Find spatial and temporal patterns
4. Identify problematic ships
5. Find their movement data

## Import data

### Marine protected areas

Elaborate data on Marine Protected Areas (MPAs) can be found at [Protected Planet](https://www.protectedplanet.net/en/thematic-areas/wdpa?tab=WDPA). This site offers several (spatial) data exports of all protected areas in the world, with plenty of metadata and background information. The id's of Protected Planet are used by Global Fishing Watch. 

### Fishing efforts

Global Fishing Watch provide data on fishing efforts, based on AIS data. 

## References

These references provide a lot of background on using AIS, detecting certain activity (loitering, fishing, transshipment, etc.), other remote sensing technologies and applications. Some of these sources use Global Fishing Watch data (especially the sources with Kroodsma as author). All sources are useful for understanding the opportunities and limits of data and technology. The papers from Anita Graser et al are very useful for understanding how AIS or other movement data can be analysed. 

Boerder, K., Miller, N. A., & Worm, B. (2018). Global hot spots of transshipment of fish catch at sea. Science Advances, 4(7), 7159–7184. [DOI](https://doi.org/10.1126/sciadv.aat7159)

Ford, J. H., Peel, D., Kroodsma, D., Hardesty, B. D., Rosebrock, U., & Wilcox, C. (2018). Detecting suspicious activities at sea based on anomalies in Automatic Identification Systems transmissions. PLoS ONE, 13(8). [DOI}(https://doi.org/10.1371/journal.pone.0201640)

Graser, A., Dragaschnig, M., Widhalm, P., Koller, H., & Brandle, N. (2020). Exploratory Trajectory Analysis for Massive Historical AIS Datasets. Proceedings - IEEE International Conference on Mobile Data Management, 2020-June, 252–257. [DOI](https://doi.org/10.1109/MDM48529.2020.00059)

Graser, A., Widhalm, P., & Dragaschnig, M. (2020). The M3 massive movement model: a distributed incrementally updatable solution for big movement data exploration. International Journal of Geographical Information Science, 34(12), 2517–2540. [DOI](https://doi.org/10.1080/13658816.2020.1776293)

Holmes, S., Natale, F., Gibin, M., Guillen, J., Alessandrini, A., Vespe, M., & Osio, G. C. (2020). Where did the vessels go? An analysis of the EU fishing fleet gravitation between home ports, fishing grounds, landing ports and markets. PLoS ONE, 15(5). [DOI](https://doi.org/10.1371/journal.pone.0230494)

Kroodsma, D. A., Mayorga, J., Hochberg, T., Miller, N. A., Boerder, K., Ferretti, F., Wilson, A., Bergman, B., White, T. D., Block, B. A., Woods, P., Sullivan, B., Costello, C., & Worm, B. (2018). Tracking the global footprint of fisheries. Science, 359(6378), 904–908. [DOI](https://doi.org/10.1126/science.aao5646)

Kroodsma, D. A., Hochberg, T., Davis, P. B., Paolo, F. S., Joo, R., & Wong, B. A. (2022). Revealing the global longline fleet with satellite radar. Scientific Reports, 12(1), 1–12. [DOI](https://doi.org/10.1038/s41598-022-23688-7)

Mazzarella, F., Vespe, M., Damalas, D., & Osio, G. (2014). Discovering vessel activities at sea using AIS data: Mapping of fishing footprints. FUSION 2014 - 17th International Conference on Information Fusion, July.

Li, M. L., Ota, Y., Underwood, P. J., Reygondeau, G., Seto, K., Lam, V. W. Y., Kroodsma, D., & Cheung, W. W. L. (2021). Tracking industrial fishing activities in African waters from space. Fish and Fisheries, 22(4), 851–864. [DOI](https://doi.org/10.1111/faf.12555)

Park, J., Lee, J., Seto, K., Hochberg, T., Wong, B. A., Miller, N. A., Takasaki, K., Kubota, H., Oozeki, Y., Doshi, S., Midzik, M., Hanich, Q., Sullivan, B., Woods, P., & Kroodsma, D. A. (2020). Illuminating dark fishing fleets in North Korea. Science Advances, 6(30). [DOI](https://doi.org/10.1126/SCIADV.ABB1197/SUPPL_FILE/ABB1197_SM.PDF)

Park, J., Van Osdel, J., Turner, J., Farthing, C. M., Miller, N. A., Linder, H. L., Crespo, G. O., Carmine, G., & Kroodsma, D. A. (2023). Tracking elusive and shifting identities of the global fishing fleet. Science Advances, 9(3). [DOI](https://doi.org/10.1126/sciadv.abp8200)

Vespe, M., Gibin, M., Alessandrini, A., Natale, F., Mazzarella, F., & Osio, G. C. (2016). Mapping EU fishing activities using ship tracking data. Journal of Maps, 12, 520–525. [DOI](https://doi.org/10.1080/17445647.2016.1195299)

Welch, H., Clavelle, T., White, T. D., Cimino, M. A., Van Osdel, J., Hochberg, T., Kroodsma, D., & Hazen, E. L. (2022). Hot spots of unseen fishing vessels. Science Advances, 8(44), 2109. [DOI](https://doi.org/10.1126/SCIADV.ABQ2109/SUPPL_FILE/SCIADV.ABQ2109_SM.PDF)

Wolsing, K., Roepert, L., Bauer, J., & Wehrle, K. (2022). Anomaly Detection in Maritime AIS Tracks: A Review of Recent Approaches. In Journal of Marine Science and Engineering (Vol. 10, Issue 1, p. 112). Multidisciplinary Digital Publishing Institute. [DOI](https://doi.org/10.3390/jmse10010112)
