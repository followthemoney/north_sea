'''
This config file contains dictionaries used for importing and cleaning
infrastructure data. Changes in sources can be made here to keep the 
other code as clean as possible.'''


# Spatial fossil fuel data urls

fossil_fuel_urls = {'no': 'https://factpages.npd.no/downloads/fgdb/NPD_FactMapsData_v3_0.zip',
					'uk': 'https://datanstauthority.blob.core.windows.net/external/OpenDataZips/UKCS_OFF_ED50.zip',
					'nl': {'infra': 'https://geo.rijkswaterstaat.nl/services/ogc/gdr/kabels_en_leidingen_noordzee/ows?',
						   'licences': 'https://www.gdngeoservices.nl/arcgis/services/nlog/gdw_ng_licence_utm/MapServer/WFSServer?',
						   'fields': 'https://www.nlog.nl/arcgis/services/NLOG_WFS/gdw_ng_wfs_field_utm/MapServer/WFSServer?',
						   'https://www.nlog.nl/arcgis/services/NLOG_WFS/gdw_ng_wfs_wll_utm/MapServer/WFSServer?'},
					'int': 'https://ows.emodnet-humanactivities.eu/wfs?SERVICE%3DWFS&REQUEST%3DGetCapabilities&VERSION=2.0.0'
					}

# Columns for cleaning


infra_cols_nl = {'facility_d': 'feature_id',
	             'facility_n': 'infra_name',
	             'status': 'status',
	             'type': 'infra_type',
	             'operator': 'operator',
	             'geometry': 'geometry',
	             'facility_c': 'description'
	             }

infra_cols_no = {'fclnpdidfacility': 'feature_id',
             	 'fclname': 'infra_name',
             	 'fclkind': 'infra_type',
             	 'fclphase': 'status',
             	 'fclcurrentoperatorname': 'operator',
             	 'fclfunctions': 'description',
             	 'geometry': 'geometry'
             	 }             

infra_cols_uk = {'feature_id': 'feature_id',
				 'status': 'status',
                 'operator': 'operator',
              	 'geometry': 'geometry',
              	 'name': 'infra_name',
              	 'infrastructure_type': 'infra_type',
              	 'description': 'description'
              	 }

infra_cols_int = {'platformid': 'feature_id',
				  'name': 'infra_name',
				  'operator': 'operator',
				  'current_status': 'status',
				  'remarks': 'description',
				  'geometry': 'geometry',
				  'category': 'infra_type',
				  'country': 'country'
				  }

pipes_cols_uk = {'feature_id': 'feature_id',
				 'pipe_name': 'infra_name',
				 'inf_type': 'infra_type',
				 'rep_group': 'operator',
				 'descriptio': 'description',
				 'status': 'status',
				 'geometry': 'geometry'
				 }

pipes_cols_nl = {'id': 'feature_id',
				 'leid_nr': 'infra_name',
				 'type': 'infra_type',
				 'operator': 'operator',
				 'opmerking': 'description',
				 'eigenaar': 'owner',
				 'status': 'status',
				 'geometry': 'geometry'
				 }

pipes_cols_no = {'pplnpdidpipeline': 'feature_id',
				 'pplname': 'infra_name',
				 'pplcurrentphase': 'status',
				 'cmplongname': 'operator',
				 'pplbelongstoname': 'owner',
				 'geometry': 'geometry'
				 }

pipes_cols_int = {'id': 'feature_id', 
				  'status': 'status', 
				  'operator': 'operator',
				  'country': 'country',
				  'geometry': 'geometry',
				  'name': 'infra_name',
				  'medium': 'description'
				  }

wells_cols_uk = {'wellregno': 'feature_id',
				  'name': 'infra_name',
				  'subareaop': 'operator',
				  'complestat': 'status',
				  'geometry': 'geometry',
				  'compledate': 'end_date',
				  'spuddate': 'start_date',
				  'origintent': 'purpose'
				  }

wells_cols_no = {'wlbnpdidwellbore': 'feature_id',
				 'wlbwellborename': 'infra_name',
				 'wlbwelltype': 'infra_type',
				 'wlbdrillingoperator': 'operator',
				 'geometry': 'geometry',
				 'wlbentrydate': 'start_date',
				 'wlbcompletiondate': 'end_date',
				 'wlbstatus': 'status'
				 }

wells_cols_nl = {'objectid': 'feature_id',
				 'identification': 'infra_name',
				 'operator': 'operator',
				 'start_date_drilling': 'start_date',
				 'end_date_drilling': 'end_date',
				 'well_type': 'infra_type',
				 'status': 'status',
				 'geometry': 'geometry'
				 }

wells_cols_int = {'code': 'feature_id',
				  'status': 'status',
				  'country': 'country',
				  'name': 'infra_name',
				  'year': 'start_date',
				  'operator': 'operator',
				  'geometry': 'geometry',
				  'purpose': 'infra_type'
				  }

# Cleaning infrastructure status

infra_status = {'In gebruik': 'In use',
               'Verwijderd': 'Removed',
               'Buiten gebruik gesteld': 'Not in use',
               'Niet in gebruik': 'Not in use',
			   'SHUT DOWN': 'Not in use', #With NOT IN USE we don't know if it's been removed.
               'IN SERVICE': 'In use',
               'INSTALLATION': 'Other',
               'PRECOMMISSIONED': 'Planned', #It's a broad term, but with planned, the platforms aren't built yet
               'DECOMMISSIONED OR REMOVED': 'Removed', #To be honest: we don't yet know if decommissioned actually means 'removed'
               'DECOMMISSIONED': 'Removed',
               'FUTURE': 'Planned',
               'PARTLY REMOVED': 'Partly removed', # We could use 'not in use as well'
               'FABRICATION': 'Planned',
               'PROPOSED': 'Planned',
               'DISPOSAL COMPLETED': 'Removed',
               'ABANDONED IN PLACE': 'Not in use',
               'LAID UP': 'Removed',
               'IN USE': 'In use',
               'ACTIVE': 'In use',
               'Active': 'In use',
               'NOT IN USE': 'Not in use',
               'ABANDONED': 'Abandoned',
               'REMOVED': 'Removed',
               'Operational': 'In use',
               'Decommissioned': 'Removed',
               'Closed down': 'Not in use',
               'Under construction': 'Planned',
               'Removed': 'Removed',
               'Abandoned': 'Not in use',
               'Pre-commissioning': 'Planned',
               'Under construction': 'Planned',
               'n/a': 'Other',
               'Abandoned Phase 3': 'Not in use',
               'Abandoned Phase 2': 'Not in use',
               'Abandoned Phase 1': 'Not in use',
               'Completed (Operating)': 'In use',
               'Completed (Shut in)': 'Not in use',
               'Completed (Shut In)': 'Not in use',
               'Plugged': 'Not in use',
               'Drilling': 'In use',
               'P&A': 'Not in use',
               'PLUGGED': 'Not in use',
               'PRODUCING': 'In use',
               'CLOSED': 'Not in use',
               'INJECTING': 'In use',
               'WILL NEVER BE DRILLED': 'Not in use',
               'SUSPENDED': 'Not in use',
               'JUNKED': 'Not in use',
               'RE-CLASS TO DEV': 'Other',
               'PREDRILLED': 'Planned',
               'DRILLING': 'Planned', 
               'RE-CLASS TO TEST': 'Other',
               'BLOWOUT': 'Not in use',
               'Producing/Injecting': 'In use',
               'Plugged back and sidetracked': 'In use',
               'Closed-in': 'Not in use',
               'Suspended': 'Not in use',
               'Observing': 'In use',
               'Plugged': 'Not in use',
               'Completed to well': 'In use',
               'N/A': 'Other',
               'Proposed': 'Planned'
	            }

# Cleaning infrastructure types

infra_types = {'Productieplatform': 'Platform',
				'Productiesatelliet': 'Platform',
				'Productielocatie': 'Platform',
				'Plant': 'Other',
				'Geothermie installatie': 'Other',
				'Subsea': 'Platforms',
				'Sidetap': 'Other',
				'Tanker mooring and loading system': 'Other',
				'Off-load Terminal': 'Other',
				'Raffinaderij': 'Other',
				'MULTI WELL TEMPLATE': 'Template',
				'RISER': 'Other',
				'MONOTOWER': 'Other',
				'SINGLE WELL TEMPLATE': 'Template',
				'SUBSEA STRUCTURE': 'Other',
				'VESSEL': 'Other',
				'ONSHORE FACILITY': 'Other',
				'LOADING SYSTEM': 'Other',
				'OFFSHORE WIND': 'Other',
				'LANDFALL': 'Other',
				'CONCRETE STRUCTURE': 'Other',
				'MOPUStor': 'Platform',
				'DORIS': 'Platform',
				'TLP STEEL': 'Platform',
				'TLP CONCRETE': 'Platform',
				'SEMISUB STEEL': 'Platform',
		        'JACKET 4 LEGS': 'Platform',
		        'JACK-UP 3 LEGS': 'Platform',
		        'JACKET 8 LEGS': 'Platform',
		        'JACKET TRIPOD': 'Platform',
		        'SPAR': 'Platform',
		        'JACKET 12 LEGS': 'Platform',
		        'CONDEEP 4 SHAFTS': 'Platform',
		        'JACKET 6 LEGS': 'Platform',
		        'JACK-UP 4 LEGS': 'Platform',
		        'CONDEEP 3 SHAFTS': 'Platform',
		        'CONDEEP MONOSHAFT': 'Platform',
		        'MATTRESS': 'Other',
		        'PROTECTION': 'Other',
		        'WELLHEAD': 'Other',
		        'OTHER SUBSEA': 'Other',
		        'ROCK DUMP': 'Other',
		        'MANIFOLD': 'Other',
		        'ANCHOR': 'Other',
		        'VALVE': 'Other',
		        'PLATFORM': 'Platform',
		        'RISER BASE': 'Other',
		        'ANCHOR PILE': 'Other',
				'ANODE ASSEMBLY': 'Other',
				'DEBRIS': 'Other',
				'PIPE JUNCTION': 'Other',
				'TOWHEAD': 'Other',
				'SPOOL PIECE': 'Other',
				'TEMPLATE': 'Template',
				'TEE PIECE': 'Other',
				'SUBSEA BUOY': 'Other',	
				'OBSTRUCTION': 'Other',
				'SEABED FASTENER': 'Other',
				'PILE': 'Other',
				'FPSO': 'Platform',
				'TERMINAL': 'Other',
				'ANCHOR BLOCK': 'Other', 
				'BUOY': 'Other',
				'STORAGE TANK': 'Other',
				'PIG LAUNCH/TRAP': 'Other',
				'OTHER SURFACE': 'Other',
				'MONITOR BUOY': 'Other',
				'SBM': 'Platform',
				'FSO': 'Platform',
				'Subsea steel': 'Platform',
				'Fixed steel': 'Platform',
				'PLATFORM': 'Platform',
				'BUOY': 'Other',
				'Floating steel': 'Platform',
				'Gravity-based concrete': 'Platform',
				'OTHER SURFACE': 'Other',
				'MONITOR BUOY': 'Other',
				'Floating concrete': 'Other',
				'SBM': 'Platform',
				'Others': 'Other',
				'BERM': 'Other',
				'PIPELINE': 'Pipeline',
				'UMBILICAL': 'Umbilical',
				'Pijpleiding': 'Pipeline',
				'DEVELOPMENT': 'Development well',
				'EXPLORATION': 'Exploration well',
				'OTHER': 'Other', 
				'Appraisal': 'Exploration well',
				'Ontwikkeling koolwaterstof': 'Development well',
				'Exploratie koolwaterstof': 'Exploration well',
				'Evaluatie koolwaterstof': 'Exploration well',
				'Ontwikkeling koolwaterstof door injectie': 'Development well',
				'Exploratie': 'Exploration well',
				'Observatie': 'Other',
				'Onbekend': 'Other',
				'Geologische verkenning': 'Exploration well',
				'Exploitation': 'Development well', 
				'FSU': 'Other',
				'SEMISUB CONCRETE': 'Other'
				}

Cleaning infrastructure result

well_results = {'Dry': 'dry',
	           'Condensate, , Oil': 'condensate,oil',
	           'Condensate, Gas': 'condensate,gas', 
	           'Condensate, Gas, Oil': 'condensate,gas,oil', 
	           'Technisch mislukt': 'failed', 
	           'Bronwater': 'water', 
	           'OIL SHOWS': 'oil', 
	           'Oil, Water': 'oil,water', 
	           'CUTTINGS': 'cuttings', 
	           'Olie shows': 'oil', 
	           'GAS SHOWS': 'gas', 
	           'Olie met gas shows': 'gas,oil', 
	           'Gas en olie shows': 'gas,oil', 
	           'Other': 'unknown', 
	           'Gas shows': 'gas', 
	           'GAS/CONDENSATE': 'condensate,gas', 
	           'CO2': 'co2', 
	           'OIL': 'oil', 
	           'OIL/GAS SHOWS': 'gas,oil', 
	           'Gas met olie shows': 'gas,oil', 
	           'OIL/GAS': 'gas,oil', 
	           'nan': 'unknown', 
	           'DRY': 'dry', 
	           'Condensate': 'condensate', 
	           'Olie': 'oil', 
	           'GAS': 'gas', 
	           'SHOWS': 'unknown', 
	           'Gas': 'gas', 
	           'NOT AVAILABLE': 'unknown', 
	           'WATER/GAS': 'gas,water', 
	           'Condensate, Gas, , Water': 'condensate,gas,water', 
	           'Onbekend': 'unknown', 
	           'Natural Gas': 'gas', 
	           'Water': 'water', 
	           'Droog': 'dry', 
	           'Olie en gas': 'gas,oil', 
	           'Gas, Oil': 'gas,oil', 
	           'OIL/GAS/CONDENSATE': 'condensate,gas,oil', 
	           'NOT APPLICABLE': 'unknown', 
	           'WATER': 'water', 
	           'Oil': 'oil', 
	           'Crude Oil': 'oil'}




