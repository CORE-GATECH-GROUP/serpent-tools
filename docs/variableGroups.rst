.. _variable-groups:

===============
Variable Groups
===============

The |BranchingReader| and |ResultsReader| can also be used to store cross sections 
and other group constant data on
:class:`~serpentTools.objects.HomogUniv` objects.
The group constants to be stored are controlled by two distinct settings:
:ref:`xs-variableExtras` and :ref:`xs-variableGroups`.
The former includes the names of Serpent variables **exactly** how they
appear in the specific output file.
The latter variables that are commonly grouped together, such
as kinetic parameters or general cross sections, without having to exactly
specify the names of each variable.
Without adjusting these settings, the |BranchingReader| and |ResultsReader| will store all data
present in the file.

Below are the various variable groups that can be used in the 
:ref:`xs-variableGroups` setting. These groups follow an inheritance-like 
pattern. For example, using Serpent 2.1.30, any group not directly placed
in the :ref:`vars-2-1-30` block, such as ``eig``, will be replaced by those
variables present in the :ref:`vars-base` block. 

Below are the variable groups that correspond to each version of Serpent
supported by this project. Under each block, such as :ref:`six-ff-2-1-30`, 
are the original ``SERPENT_STYLE_VARIABLES`` and their corresponding
variable names converted to ``mixedCaseNames``. This conversion is done
to fit the style of the project and reduce a few keystrokes for accessing
variable names.

.. _vars-2-1-31:

----------
``2.1.31``
----------

Variable groups for Serpent 2.1.31 are identical to those from 
Serpent 2.1.30

.. _vars-2-1-30:

----------
``2.1.30``
----------

.. _n-balance-2-1-30:


``n-balance``
-------------


  * ``BALA_LOSS_NEUTRON_CAPT`` →  ``balaLossNeutronCapt``
  * ``BALA_LOSS_NEUTRON_CUT`` →  ``balaLossNeutronCut``
  * ``BALA_LOSS_NEUTRON_ERR`` →  ``balaLossNeutronErr``
  * ``BALA_LOSS_NEUTRON_FISS`` →  ``balaLossNeutronFiss``
  * ``BALA_LOSS_NEUTRON_LEAK`` →  ``balaLossNeutronLeak``
  * ``BALA_LOSS_NEUTRON_TOT`` →  ``balaLossNeutronTot``
  * ``BALA_NEUTRON_DIFF`` →  ``balaNeutronDiff``
  * ``BALA_SRC_NEUTRON_FISS`` →  ``balaSrcNeutronFiss``
  * ``BALA_SRC_NEUTRON_NXN`` →  ``balaSrcNeutronNxn``
  * ``BALA_SRC_NEUTRON_SRC`` →  ``balaSrcNeutronSrc``
  * ``BALA_SRC_NEUTRON_TOT`` →  ``balaSrcNeutronTot``
  * ``BALA_SRC_NEUTRON_VR`` →  ``balaSrcNeutronVr``

.. _optimization-2-1-30:


``optimization``
----------------


  * ``DOUBLE_INDEXING`` →  ``doubleIndexing``
  * ``MG_MAJORANT_MODE`` →  ``mgMajorantMode``
  * ``OPTIMIZATION_MODE`` →  ``optimizationMode``
  * ``RECONSTRUCT_MACROXS`` →  ``reconstructMacroxs``
  * ``RECONSTRUCT_MICROXS`` →  ``reconstructMicroxs``
  * ``SPECTRUM_COLLAPSE`` →  ``spectrumCollapse``

.. _rad-data-2-1-30:


``rad-data``
------------


  * ``ACTINIDE_ACTIVITY`` →  ``actinideActivity``
  * ``ACTINIDE_DECAY_HEAT`` →  ``actinideDecayHeat``
  * ``ACTINIDE_ING_TOX`` →  ``actinideIngTox``
  * ``ACTINIDE_INH_TOX`` →  ``actinideInhTox``
  * ``ALPHA_DECAY_SOURCE`` →  ``alphaDecaySource``
  * ``CS134_ACTIVITY`` →  ``cs134Activity``
  * ``ELECTRON_DECAY_SOURCE`` →  ``electronDecaySource``
  * ``FISSION_PRODUCT_ACTIVITY`` →  ``fissionProductActivity``
  * ``FISSION_PRODUCT_DECAY_HEAT`` →  ``fissionProductDecayHeat``
  * ``FISSION_PRODUCT_ING_TOX`` →  ``fissionProductIngTox``
  * ``FISSION_PRODUCT_INH_TOX`` →  ``fissionProductInhTox``
  * ``INGENSTION_TOXICITY`` →  ``ingenstionToxicity``
  * ``INHALATION_TOXICITY`` →  ``inhalationToxicity``
  * ``NEUTRON_DECAY_SOURCE`` →  ``neutronDecaySource``
  * ``PHOTON_DECAY_SOURCE`` →  ``photonDecaySource``
  * ``SR90_ACTIVITY`` →  ``sr90Activity``
  * ``TE132_ACTIVITY`` →  ``te132Activity``
  * ``TOT_ACTIVITY`` →  ``totActivity``
  * ``TOT_DECAY_HEAT`` →  ``totDecayHeat``
  * ``TOT_SF_RATE`` →  ``totSfRate``

.. _six-ff-2-1-30:


``six-ff``
----------


  * ``SIX_FF_EPSILON`` →  ``sixFfEpsilon``
  * ``SIX_FF_ETA`` →  ``sixFfEta``
  * ``SIX_FF_F`` →  ``sixFfF``
  * ``SIX_FF_KEFF`` →  ``sixFfKeff``
  * ``SIX_FF_KINF`` →  ``sixFfKinf``
  * ``SIX_FF_LF`` →  ``sixFfLf``
  * ``SIX_FF_LT`` →  ``sixFfLt``
  * ``SIX_FF_P`` →  ``sixFfP``

.. _vars-base:

--------
``base``
--------

.. _adf-base:


``adf``
-------


  * ``DF_CORN_AREA`` →  ``dfCornArea``
  * ``DF_CORN_DF`` →  ``dfCornDf``
  * ``DF_CORN_IN_CURR`` →  ``dfCornInCurr``
  * ``DF_CORN_NET_CURR`` →  ``dfCornNetCurr``
  * ``DF_CORN_OUT_CURR`` →  ``dfCornOutCurr``
  * ``DF_HET_CORN_FLUX`` →  ``dfHetCornFlux``
  * ``DF_HET_SURF_FLUX`` →  ``dfHetSurfFlux``
  * ``DF_HET_VOL_FLUX`` →  ``dfHetVolFlux``
  * ``DF_HOM_CORN_FLUX`` →  ``dfHomCornFlux``
  * ``DF_HOM_SURF_FLUX`` →  ``dfHomSurfFlux``
  * ``DF_HOM_VOL_FLUX`` →  ``dfHomVolFlux``
  * ``DF_MID_AREA`` →  ``dfMidArea``
  * ``DF_MID_IN_CURR`` →  ``dfMidInCurr``
  * ``DF_MID_NET_CURR`` →  ``dfMidNetCurr``
  * ``DF_MID_OUT_CURR`` →  ``dfMidOutCurr``
  * ``DF_N_CORN`` →  ``dfNCorn``
  * ``DF_N_SURF`` →  ``dfNSurf``
  * ``DF_SURFACE`` →  ``dfSurface``
  * ``DF_SURF_AREA`` →  ``dfSurfArea``
  * ``DF_SURF_DF`` →  ``dfSurfDf``
  * ``DF_SURF_IN_CURR`` →  ``dfSurfInCurr``
  * ``DF_SURF_NET_CURR`` →  ``dfSurfNetCurr``
  * ``DF_SURF_OUT_CURR`` →  ``dfSurfOutCurr``
  * ``DF_SYM`` →  ``dfSym``
  * ``DF_VOLUME`` →  ``dfVolume``

.. _albedos-base:


``albedos``
-----------


  * ``ALB_FLIP_DIR`` →  ``albFlipDir``
  * ``ALB_IN_CURR`` →  ``albInCurr``
  * ``ALB_N_SURF`` →  ``albNSurf``
  * ``ALB_OUT_CURR`` →  ``albOutCurr``
  * ``ALB_PART_ALB`` →  ``albPartAlb``
  * ``ALB_SURFACE`` →  ``albSurface``
  * ``ALB_TOT_ALB`` →  ``albTotAlb``

.. _arr-estimators-base:


``arr-estimators``
------------------


  * ``CONVERSION_RATIO`` →  ``conversionRatio``
  * ``PU239_CAPT`` →  ``pu239Capt``
  * ``PU239_FISS`` →  ``pu239Fiss``
  * ``PU240_CAPT`` →  ``pu240Capt``
  * ``PU240_FISS`` →  ``pu240Fiss``
  * ``PU241_CAPT`` →  ``pu241Capt``
  * ``PU241_FISS`` →  ``pu241Fiss``
  * ``SM149_CAPT`` →  ``sm149Capt``
  * ``U235_CAPT`` →  ``u235Capt``
  * ``U235_FISS`` →  ``u235Fiss``
  * ``U238_CAPT`` →  ``u238Capt``
  * ``U238_FISS`` →  ``u238Fiss``
  * ``XE135_CAPT`` →  ``xe135Capt``

.. _burnup-coeff-base:


``burnup-coeff``
----------------


  * ``BURNUP`` →  ``burnup``
  * ``BURN_DAYS`` →  ``burnDays``
  * ``BURN_MATERIALS`` →  ``burnMaterials``
  * ``BURN_MODE`` →  ``burnMode``
  * ``BURN_STEP`` →  ``burnStep``
  * ``COEF_BRANCH`` →  ``coefBranch``
  * ``COEF_BU_STEP`` →  ``coefBuStep``
  * ``COEF_IDX`` →  ``coefIdx``

.. _diffusion-base:


``diffusion``
-------------


  * ``CMM_DIFFCOEF`` →  ``cmmDiffcoef``
  * ``CMM_DIFFCOEF_X`` →  ``cmmDiffcoefX``
  * ``CMM_DIFFCOEF_Y`` →  ``cmmDiffcoefY``
  * ``CMM_DIFFCOEF_Z`` →  ``cmmDiffcoefZ``
  * ``CMM_TRANSPXS`` →  ``cmmTranspxs``
  * ``CMM_TRANSPXS_X`` →  ``cmmTranspxsX``
  * ``CMM_TRANSPXS_Y`` →  ``cmmTranspxsY``
  * ``CMM_TRANSPXS_Z`` →  ``cmmTranspxsZ``

.. _eig-base:


``eig``
-------


  * ``ABS_KEFF`` →  ``absKeff``
  * ``ABS_KINF`` →  ``absKinf``
  * ``ANA_KEFF`` →  ``anaKeff``
  * ``COL_KEFF`` →  ``colKeff``
  * ``GEOM_ALBEDO`` →  ``geomAlbedo``
  * ``IMP_KEFF`` →  ``impKeff``

.. _files-base:


``files``
---------


  * ``BRA_DATA_DILE_PATH`` →  ``braDataDilePath``
  * ``DECAY_DATA_DILE_PATH`` →  ``decayDataDilePath``
  * ``NFY_DATA_DILE_PATH`` →  ``nfyDataDilePath``
  * ``SFY_DATA_DILE_PATH`` →  ``sfyDataDilePath``
  * ``XS_DATA_FILE_PATH`` →  ``xsDataFilePath``

.. _gc-meta-base:


``gc-meta``
-----------


  * ``GC_UNIVERSE_NAME`` →  ``gcUniverseName``
  * ``INF_FISS_FLX`` →  ``infFissFlx``
  * ``INF_FLX`` →  ``infFlx``
  * ``INF_KINF`` →  ``infKinf``
  * ``INF_MICRO_FLX`` →  ``infMicroFlx``
  * ``MACRO_E`` →  ``macroE``
  * ``MACRO_NG`` →  ``macroNg``
  * ``MICRO_E`` →  ``microE``
  * ``MICRO_NG`` →  ``microNg``

.. _kinetics-base:


``kinetics``
------------


  * ``ADJ_IFP_ANA_BETA_EFF`` →  ``adjIfpAnaBetaEff``
  * ``ADJ_IFP_ANA_LAMBDA`` →  ``adjIfpAnaLambda``
  * ``ADJ_IFP_GEN_TIME`` →  ``adjIfpGenTime``
  * ``ADJ_IFP_IMP_BETA_EFF`` →  ``adjIfpImpBetaEff``
  * ``ADJ_IFP_IMP_LAMBDA`` →  ``adjIfpImpLambda``
  * ``ADJ_IFP_LIFETIME`` →  ``adjIfpLifetime``
  * ``ADJ_IFP_ROSSI_ALPHA`` →  ``adjIfpRossiAlpha``
  * ``ADJ_INV_SPD`` →  ``adjInvSpd``
  * ``ADJ_MEULEKAMP_BETA_EFF`` →  ``adjMeulekampBetaEff``
  * ``ADJ_MEULEKAMP_LAMBDA`` →  ``adjMeulekampLambda``
  * ``ADJ_NAUCHI_BETA_EFF`` →  ``adjNauchiBetaEff``
  * ``ADJ_NAUCHI_GEN_TIME`` →  ``adjNauchiGenTime``
  * ``ADJ_NAUCHI_LAMBDA`` →  ``adjNauchiLambda``
  * ``ADJ_NAUCHI_LIFETIME`` →  ``adjNauchiLifetime``
  * ``ADJ_PERT_BETA_EFF`` →  ``adjPertBetaEff``
  * ``ADJ_PERT_GEN_TIME`` →  ``adjPertGenTime``
  * ``ADJ_PERT_LIFETIME`` →  ``adjPertLifetime``
  * ``ADJ_PERT_ROSSI_ALPHA`` →  ``adjPertRossiAlpha``
  * ``BETA_EFF`` →  ``betaEff``
  * ``FWD_ANA_BETA_ZERO`` →  ``fwdAnaBetaZero``
  * ``FWD_ANA_LAMBDA`` →  ``fwdAnaLambda``
  * ``LAMBDA`` →  ``lambda``

.. _lifetime-base:


``lifetime``
------------


  * ``ANA_DELAYED_EMTIME`` →  ``anaDelayedEmtime``
  * ``ANA_MEAN_NCOL`` →  ``anaMeanNcol``
  * ``ANA_SLOW_TIME`` →  ``anaSlowTime``
  * ``ANA_THERM_FRAC`` →  ``anaThermFrac``
  * ``ANA_THERM_TIME`` →  ``anaThermTime``

.. _memory-base:


``memory``
----------


  * ``ALLOC_MEMSIZE`` →  ``allocMemsize``
  * ``AVAIL_MEM`` →  ``availMem``
  * ``MAT_MEMSIZE`` →  ``matMemsize``
  * ``MEMSIZE`` →  ``memsize``
  * ``MISC_MEMSIZE`` →  ``miscMemsize``
  * ``RES_MEMSIZE`` →  ``resMemsize``
  * ``UNKNOWN_MEMSIZE`` →  ``unknownMemsize``
  * ``UNUSED_MEMSIZE`` →  ``unusedMemsize``
  * ``XS_MEMSIZE`` →  ``xsMemsize``

.. _misc-base:


``misc``
--------


  * ``ANA_AFGE`` →  ``anaAfge``
  * ``ANA_ALF`` →  ``anaAlf``
  * ``ANA_EALF`` →  ``anaEalf``
  * ``FISSE`` →  ``fisse``
  * ``IMP_AFGE`` →  ``impAfge``
  * ``IMP_ALF`` →  ``impAlf``
  * ``IMP_EALF`` →  ``impEalf``
  * ``NUBAR`` →  ``nubar``

.. _n-balance-base:


``n-balance``
-------------


  * ``BALA_LOSS_NEUTRON_CAPT`` →  ``balaLossNeutronCapt``
  * ``BALA_LOSS_NEUTRON_CUT`` →  ``balaLossNeutronCut``
  * ``BALA_LOSS_NEUTRON_FISS`` →  ``balaLossNeutronFiss``
  * ``BALA_LOSS_NEUTRON_LEAK`` →  ``balaLossNeutronLeak``
  * ``BALA_LOSS_NEUTRON_TOT`` →  ``balaLossNeutronTot``
  * ``BALA_NEUTRON_DIFF`` →  ``balaNeutronDiff``
  * ``BALA_SRC_NEUTRON_FISS`` →  ``balaSrcNeutronFiss``
  * ``BALA_SRC_NEUTRON_NXN`` →  ``balaSrcNeutronNxn``
  * ``BALA_SRC_NEUTRON_SRC`` →  ``balaSrcNeutronSrc``
  * ``BALA_SRC_NEUTRON_TOT`` →  ``balaSrcNeutronTot``
  * ``BALA_SRC_NEUTRON_VR`` →  ``balaSrcNeutronVr``

.. _neutron-physics-base:


``neutron-physics``
-------------------


  * ``DOPPLER_PREPROCESSOR`` →  ``dopplerPreprocessor``
  * ``IMPL_CAPT`` →  ``implCapt``
  * ``IMPL_FISS`` →  ``implFiss``
  * ``IMPL_NXN`` →  ``implNxn``
  * ``NEUTORN_ERG_NE`` →  ``neutornErgNe``
  * ``NEUTRON_EMAX`` →  ``neutronEmax``
  * ``NEUTRON_EMIN`` →  ``neutronEmin``
  * ``NEUTRON_ERG_TOL`` →  ``neutronErgTol``
  * ``SAMPLE_CAPT`` →  ``sampleCapt``
  * ``SAMPLE_FISS`` →  ``sampleFiss``
  * ``SAMPLE_SCATT`` →  ``sampleScatt``
  * ``TMS_MODE`` →  ``tmsMode``
  * ``USE_DBRC`` →  ``useDbrc``
  * ``USE_DELNU`` →  ``useDelnu``
  * ``USE_URES`` →  ``useUres``

.. _nuclides-base:


``nuclides``
------------


  * ``TOT_DECAY_NUCLIDES`` →  ``totDecayNuclides``
  * ``TOT_DOSIMETRY_NUCLIDES`` →  ``totDosimetryNuclides``
  * ``TOT_NUCLIDES`` →  ``totNuclides``
  * ``TOT_PHOTON_NUCLIDES`` →  ``totPhotonNuclides``
  * ``TOT_REA_CHANNELS`` →  ``totReaChannels``
  * ``TOT_TRANSMU_REA`` →  ``totTransmuRea``
  * ``TOT_TRANSPORT_NUCLIDES`` →  ``totTransportNuclides``

.. _optimization-base:


``optimization``
----------------


  * ``MG_MAJORANT_MODE`` →  ``mgMajorantMode``
  * ``OPTIMIZATION_MODE`` →  ``optimizationMode``
  * ``RECONSTRUCT_MACROXS`` →  ``reconstructMacroxs``
  * ``RECONSTRUCT_MICROXS`` →  ``reconstructMicroxs``
  * ``SPECTRUM_COLLAPSE`` →  ``spectrumCollapse``

.. _parallel-base:


``parallel``
------------


  * ``MPI_REPRODUCIBILITY`` →  ``mpiReproducibility``
  * ``MPI_TASKS`` →  ``mpiTasks``
  * ``OMP_HISTORY_PROFILE`` →  ``ompHistoryProfile``
  * ``OMP_REPRODUCIBILITY`` →  ``ompReproducibility``
  * ``OMP_THREADS`` →  ``ompThreads``
  * ``SHARE_BUF_ARRAY`` →  ``shareBufArray``
  * ``SHARE_RES2_ARRAY`` →  ``shareRes2Array``

.. _parameters-base:


``parameters``
--------------


  * ``B1_BURNUP_CORRECTION`` →  ``b1BurnupCorrection``
  * ``B1_CALCULATION`` →  ``b1Calculation``
  * ``BATCH_INTERVAL`` →  ``batchInterval``
  * ``CYCLES`` →  ``cycles``
  * ``GROUP_CONSTANT_GENERATION`` →  ``groupConstantGeneration``
  * ``IMPLICIT_REACTION_RATES`` →  ``implicitReactionRates``
  * ``NEUTRON_TRANSPORT_MODE`` →  ``neutronTransportMode``
  * ``PHOTON_TRANSPORT_MODE`` →  ``photonTransportMode``
  * ``POP`` →  ``pop``
  * ``SEED`` →  ``seed``
  * ``SKIP`` →  ``skip``
  * ``SRC_NORM_MODE`` →  ``srcNormMode``
  * ``UFS_MODE`` →  ``ufsMode``
  * ``UFS_ORDER`` →  ``ufsOrder``

.. _pin-power-base:


``pin-power``
-------------


  * ``PPW_FF`` →  ``ppwFf``
  * ``PPW_HOM_FLUX`` →  ``ppwHomFlux``
  * ``PPW_LATTICE`` →  ``ppwLattice``
  * ``PPW_LATTICE_TYPE`` →  ``ppwLatticeType``
  * ``PPW_PINS`` →  ``ppwPins``
  * ``PPW_POW`` →  ``ppwPow``

.. _poisons-base:


``poisons``
-----------


  * ``I135_MICRO_ABS`` →  ``i135MicroAbs``
  * ``I135_YIELD`` →  ``i135Yield``
  * ``PM147_MICRO_ABS`` →  ``pm147MicroAbs``
  * ``PM147_YIELD`` →  ``pm147Yield``
  * ``PM148M_MICRO_ABS`` →  ``pm148mMicroAbs``
  * ``PM148M_YIELD`` →  ``pm148mYield``
  * ``PM148_MICRO_ABS`` →  ``pm148MicroAbs``
  * ``PM148_YIELD`` →  ``pm148Yield``
  * ``PM149_MICRO_ABS`` →  ``pm149MicroAbs``
  * ``PM149_YIELD`` →  ``pm149Yield``
  * ``SM149_MACRO_ABS`` →  ``sm149MacroAbs``
  * ``SM149_MICRO_ABS`` →  ``sm149MicroAbs``
  * ``SM149_YIELD`` →  ``sm149Yield``
  * ``XE135_MACRO_ABS`` →  ``xe135MacroAbs``
  * ``XE135_MICRO_ABS`` →  ``xe135MicroAbs``
  * ``XE135_YIELD`` →  ``xe135Yield``

.. _rad-data-base:


``rad-data``
------------


  * ``ACTINIDE_ACTIVITY`` →  ``actinideActivity``
  * ``ACTINIDE_DECAY_HEAT`` →  ``actinideDecayHeat``
  * ``ACTINIDE_ING_TOX`` →  ``actinideIngTox``
  * ``ACTINIDE_INH_TOX`` →  ``actinideInhTox``
  * ``ALPHA_DECAY_SOURCE`` →  ``alphaDecaySource``
  * ``BETA_DECAY_SOURCE`` →  ``betaDecaySource``
  * ``CS134_ACTIVITY`` →  ``cs134Activity``
  * ``FISSION_PRODUCT_ACTIVITY`` →  ``fissionProductActivity``
  * ``FISSION_PRODUCT_DECAY_HEAT`` →  ``fissionProductDecayHeat``
  * ``FISSION_PRODUCT_ING_TOX`` →  ``fissionProductIngTox``
  * ``FISSION_PRODUCT_INH_TOX`` →  ``fissionProductInhTox``
  * ``INGENSTION_TOXICITY`` →  ``ingenstionToxicity``
  * ``INHALATION_TOXICITY`` →  ``inhalationToxicity``
  * ``NEUTRON_DECAY_SOURCE`` →  ``neutronDecaySource``
  * ``PHOTON_DECAY_SOURCE`` →  ``photonDecaySource``
  * ``SR90_ACTIVITY`` →  ``sr90Activity``
  * ``TE132_ACTIVITY`` →  ``te132Activity``
  * ``TOT_ACTIVITY`` →  ``totActivity``
  * ``TOT_DECAY_HEAT`` →  ``totDecayHeat``
  * ``TOT_SF_RATE`` →  ``totSfRate``

.. _sampling-base:


``sampling``
------------


  * ``AVG_REAL_COL`` →  ``avgRealCol``
  * ``AVG_SURF_CROSS`` →  ``avgSurfCross``
  * ``AVG_TRACKING_LOOPS`` →  ``avgTrackingLoops``
  * ``AVG_TRACKS`` →  ``avgTracks``
  * ``AVG_VIRT_COL`` →  ``avgVirtCol``
  * ``DT_EFF`` →  ``dtEff``
  * ``DT_FRAC`` →  ``dtFrac``
  * ``DT_THRESH`` →  ``dtThresh``
  * ``LOST_PARTICLES`` →  ``lostParticles``
  * ``MIN_MACROXS`` →  ``minMacroxs``
  * ``REA_SAMPLING_EFF`` →  ``reaSamplingEff``
  * ``REA_SAMPLING_FAIL`` →  ``reaSamplingFail``
  * ``ST_FRAC`` →  ``stFrac``
  * ``TOT_COL_EFF`` →  ``totColEff``

.. _stats-base:


``stats``
---------


  * ``CYCLE_IDX`` →  ``cycleIdx``
  * ``MEAN_POP_SIZE`` →  ``meanPopSize``
  * ``MEAN_POP_WGT`` →  ``meanPopWgt``
  * ``SIMULATION_COMPLETED`` →  ``simulationCompleted``
  * ``SOURCE_POPULATION`` →  ``sourcePopulation``

.. _times-base:


``times``
---------


  * ``BATEMAN_SOLUTION_TIME`` →  ``batemanSolutionTime``
  * ``BURNUP_CYCLE_TIME`` →  ``burnupCycleTime``
  * ``CPU_USAGE`` →  ``cpuUsage``
  * ``ESTIMATED_RUNNING_TIME`` →  ``estimatedRunningTime``
  * ``INIT_TIME`` →  ``initTime``
  * ``MPI_OVERHEAD_TIME`` →  ``mpiOverheadTime``
  * ``OMP_PARALLEL_FRAC`` →  ``ompParallelFrac``
  * ``PROCESS_TIME`` →  ``processTime``
  * ``RUNNING_TIME`` →  ``runningTime``
  * ``TOT_CPU_TIME`` →  ``totCpuTime``
  * ``TRANSPORT_CPU_USAGE`` →  ``transportCpuUsage``
  * ``TRANSPORT_CYCLE_TIME`` →  ``transportCycleTime``

.. _total-rr-base:


``total-rr``
------------


  * ``ALBEDO_LEAKRATE`` →  ``albedoLeakrate``
  * ``INI_BURN_FMASS`` →  ``iniBurnFmass``
  * ``INI_FMASS`` →  ``iniFmass``
  * ``TOT_ABSRATE`` →  ``totAbsrate``
  * ``TOT_BURN_FMASS`` →  ``totBurnFmass``
  * ``TOT_CAPTRATE`` →  ``totCaptrate``
  * ``TOT_CUTRATE`` →  ``totCutrate``
  * ``TOT_FISSRATE`` →  ``totFissrate``
  * ``TOT_FLUX`` →  ``totFlux``
  * ``TOT_FMASS`` →  ``totFmass``
  * ``TOT_GENRATE`` →  ``totGenrate``
  * ``TOT_LOSSRATE`` →  ``totLossrate``
  * ``TOT_PHOTON_PRODRATE`` →  ``totPhotonProdrate``
  * ``TOT_POWDENS`` →  ``totPowdens``
  * ``TOT_POWRER`` →  ``totPowrer``
  * ``TOT_RR`` →  ``totRr``
  * ``TOT_SRCRATE`` →  ``totSrcrate``

.. _ures-base:


``ures``
--------


  * ``URES_AVAIL`` →  ``uresAvail``
  * ``URES_DILU_CUT`` →  ``uresDiluCut``
  * ``URES_EMAX`` →  ``uresEmax``
  * ``URES_EMIN`` →  ``uresEmin``
  * ``URES_SEED`` →  ``uresSeed``

.. _versions-base:


``versions``
------------


  * ``COMPILE_DATE`` →  ``compileDate``
  * ``COMPLETE_DATE`` →  ``completeDate``
  * ``CONFIDENTIAL_DATA`` →  ``confidentialData``
  * ``CPU_MHZ`` →  ``cpuMhz``
  * ``CPU_TYPE`` →  ``cpuType``
  * ``DEBUG`` →  ``debug``
  * ``HOSTNAME`` →  ``hostname``
  * ``INPUT_FILE_NAME`` →  ``inputFileName``
  * ``START_DATE`` →  ``startDate``
  * ``TITLE`` →  ``title``
  * ``VERSION`` →  ``version``
  * ``WORKING_DIRECTORY`` →  ``workingDirectory``

.. _xs-base:


``xs``
------


  * ``ABS`` →  ``abs``
  * ``CAPT`` →  ``capt``
  * ``CHID`` →  ``chid``
  * ``CHIP`` →  ``chip``
  * ``CHIT`` →  ``chit``
  * ``DIFFCOEF`` →  ``diffcoef``
  * ``FISS`` →  ``fiss``
  * ``INVV`` →  ``invv``
  * ``KAPPA`` →  ``kappa``
  * ``NSF`` →  ``nsf``
  * ``NUBAR`` →  ``nubar``
  * ``RABSXS`` →  ``rabsxs``
  * ``REMXS`` →  ``remxs``
  * ``S0`` →  ``s0``
  * ``S1`` →  ``s1``
  * ``S2`` →  ``s2``
  * ``S3`` →  ``s3``
  * ``S4`` →  ``s4``
  * ``S5`` →  ``s5``
  * ``S6`` →  ``s6``
  * ``S7`` →  ``s7``
  * ``SCATT0`` →  ``scatt0``
  * ``SCATT1`` →  ``scatt1``
  * ``SCATT2`` →  ``scatt2``
  * ``SCATT3`` →  ``scatt3``
  * ``SCATT4`` →  ``scatt4``
  * ``SCATT5`` →  ``scatt5``
  * ``SCATT6`` →  ``scatt6``
  * ``SCATT7`` →  ``scatt7``
  * ``TOT`` →  ``tot``
  * ``TRANSPXS`` →  ``transpxs``

.. _xs-prod-base:


``xs-prod``
-----------


  * ``SCATT2`` →  ``scatt2``
  * ``SCATTP0`` →  ``scattp0``
  * ``SCATTP1`` →  ``scattp1``
  * ``SCATTP3`` →  ``scattp3``
  * ``SCATTP4`` →  ``scattp4``
  * ``SCATTP5`` →  ``scattp5``
  * ``SCATTP6`` →  ``scattp6``
  * ``SCATTP7`` →  ``scattp7``
  * ``SP0`` →  ``sp0``
  * ``SP1`` →  ``sp1``
  * ``SP2`` →  ``sp2``
  * ``SP3`` →  ``sp3``
  * ``SP4`` →  ``sp4``
  * ``SP5`` →  ``sp5``
  * ``SP6`` →  ``sp6``
  * ``SP7`` →  ``sp7``

