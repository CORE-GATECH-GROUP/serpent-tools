
% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.29' ;
COMPILE_DATE              (idx, [1: 20])  = 'Jan 26 2018 16:56:51' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1:  8])  = 'Untitled' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1:  3])  = 'bwr' ;
WORKING_DIRECTORY         (idx, [1: 47])  = '/home/ajohnson400/research/serpent-tools/models' ;
HOSTNAME                  (idx, [1: 14])  = 'ME04L0358GRD04' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i7-6700T CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 194.0 ;
START_DATE                (idx, [1: 24])  = 'Fri Feb  2 15:15:56 2018' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Fri Feb  2 15:16:08 2018' ;

% Run parameters:

POP                       (idx, 1)        = 1000 ;
CYCLES                    (idx, 1)        = 50 ;
SKIP                      (idx, 1)        = 20 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1517602556 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, [1:  3])  = [ 0 0 0 ];
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 1 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
SHARE_BUF_ARRAY           (idx, 1)        = 1 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 22])  = '/xs/sss_endfb7u.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 18])  = '/xs/sss_endfb7.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 18])  = '/xs/sss_endfb7.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 18])  = '/xs/sss_endfb7.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 3.3E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  2.11511E-01 0.00383  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  7.88489E-01 0.00103  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  5.16315E-01 0.00185  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  5.63883E-01 0.00135  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  4.54134E+00 0.00346  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.89489E+01 0.00227  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.89489E+01 0.00227  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  2.23979E+01 0.00462  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  7.37422E+00 0.00606  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 50 ;
SOURCE_POPULATION         (idx, 1)        = 50047 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  1.00094E+03 0.00721 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  1.00094E+03 0.00721 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.95716E-01 ;
RUNNING_TIME              (idx, 1)        =  1.95700E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  3.17333E-02  3.17333E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  3.66667E-04  3.66667E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.63600E-01  1.63600E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.95667E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 1.00008 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  9.99845E-01 0.00038 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.34100E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 15935.20 ;
ALLOC_MEMSIZE             (idx, 1)        = 205.03;
MEMSIZE                   (idx, 1)        = 165.33;
XS_MEMSIZE                (idx, 1)        = 104.71;
MAT_MEMSIZE               (idx, 1)        = 53.25;
RES_MEMSIZE               (idx, 1)        = 0.76;
MISC_MEMSIZE              (idx, 1)        = 6.62;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 39.70;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 6 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 126685 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 10 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 15 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 15 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 460 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 0 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 0 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.36288E+06 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.05232E-06 ;
TOT_SF_RATE               (idx, 1)        =  1.73709E+02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.36288E+06 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.05232E-06 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.54938E+01 ;
INGESTION_TOXICITY        (idx, 1)        =  1.98693E-01 ;
ACTINIDE_INH_TOX          (idx, 1)        =  3.54938E+01 ;
ACTINIDE_ING_TOX          (idx, 1)        =  1.98693E-01 ;
FISSION_PRODUCT_INH_TOX   (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_ING_TOX   (idx, 1)        =  0.00000E+00 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
PHOTON_DECAY_SOURCE       (idx, 1)        =  1.66689E+06 ;
NEUTRON_DECAY_SOURCE      (idx, 1)        =  0.00000E+00 ;
ALPHA_DECAY_SOURCE        (idx, 1)        =  4.34600E+06 ;
BETA_DECAY_SOURCE         (idx, 1)        =  2.85539E+06 ;

% Normaliation coefficient:

NORM_COEF                 (idx, [1:   4]) = [  9.96389E-04 0.00271  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  3.99643E-01 0.01136 ];
U235_FISS                 (idx, [1:   4]) = [  3.96134E-01 0.00564  9.35123E-01 0.00196 ];
U238_FISS                 (idx, [1:   4]) = [  2.74894E-02 0.02863  6.48771E-02 0.02827 ];
U235_CAPT                 (idx, [1:   4]) = [  1.00768E-01 0.01561  1.75438E-01 0.01444 ];
U238_CAPT                 (idx, [1:   4]) = [  1.98254E-01 0.00915  3.45170E-01 0.00713 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS       (idx, [1:  2])  = [ 50047 5.00000E+04 ];
BALA_SRC_NEUTRON_NXN        (idx, [1:  2])  = [ 0 7.45234E+01 ];
BALA_SRC_NEUTRON_VR         (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT        (idx, [1:  2])  = [ 50047 5.00745E+04 ];

BALA_LOSS_NEUTRON_CAPT       (idx, [1:  2])  = [ 28791 2.88145E+04 ];
BALA_LOSS_NEUTRON_FISS       (idx, [1:  2])  = [ 21256 2.12600E+04 ];
BALA_LOSS_NEUTRON_LEAK       (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT        (idx, [1:  2])  = [ 50047 5.00745E+04 ];

BALA_NEUTRON_DIFF            (idx, [1:  2])  = [ 0 -3.63798E-11 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.37786E-11 0.00351 ];
TOT_POWDENS               (idx, [1:   2]) = [  5.09175E-17 0.00351 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.04571E+00 0.00349 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.24518E-01 0.00351 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.75482E-01 0.00259 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.96389E-01 0.00271 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.29361E+01 0.00246 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.88760E+01 0.00245 ];
INI_FMASS                 (idx, 1)        =  2.70606E-01 ;
TOT_FMASS                 (idx, 1)        =  2.70606E-01 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46329E+00 0.00014 ];
FISSE                     (idx, [1:   2]) = [  2.02580E+02 1.3E-05 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.04690E+00 0.00505  1.04060E+00 0.00501  6.88199E-03 0.08844 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.04740E+00 0.00351 ];
COL_KEFF                  (idx, [1:   2]) = [  1.04996E+00 0.00477 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.04740E+00 0.00351 ];
ABS_KINF                  (idx, [1:   2]) = [  1.04740E+00 0.00351 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.64311E+01 0.00224 ];
IMP_ALF                   (idx, [1:   2]) = [  1.64576E+01 0.00094 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.51254E-06 0.03827 ];
IMP_EALF                  (idx, [1:   2]) = [  1.43284E-06 0.01592 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.39523E-01 0.02517 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.37944E-01 0.01111 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  6.88696E-03 0.05015  1.86467E-04 0.28610  9.12521E-04 0.14804  1.17311E-03 0.12868  3.32983E-03 0.07217  9.93397E-04 0.12893  2.91640E-04 0.28005 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  6.97102E-01 0.13491  2.49811E-03 0.28571  2.03046E-02 0.10716  7.74267E-02 0.09358  3.13590E-01 0.02049  8.88208E-01 0.10255  2.13986E+00 0.25476 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  7.62745E-03 0.07592  1.84248E-04 0.49035  1.14646E-03 0.20405  1.20788E-03 0.22169  3.45117E-03 0.10925  1.13207E-03 0.18412  5.05625E-04 0.35405 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  8.83572E-01 0.19655  1.24906E-02 0.0E+00  3.17288E-02 0.00209  1.10395E-01 0.00323  3.19909E-01 0.00245  1.34783E+00 0.00156  8.89745E+00 0.01691 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.16809E-05 0.01186  2.16325E-05 0.01184  2.34221E-05 0.16972 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.26780E-05 0.01144  2.26270E-05 0.01139  2.46370E-05 0.17144 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  6.39833E-03 0.08736  1.19278E-04 0.56593  9.50047E-04 0.22255  8.92154E-04 0.27223  2.95035E-03 0.10977  1.10288E-03 0.20951  3.83635E-04 0.34575 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  8.75489E-01 0.18809  1.24906E-02 0.0E+00  3.17318E-02 0.00291  1.10132E-01 0.00495  3.20655E-01 0.00376  1.34840E+00 0.00202  8.80421E+00 0.01906 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.19182E-05 0.02572  2.19321E-05 0.02621  1.08958E-05 0.32099 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.29263E-05 0.02507  2.29417E-05 0.02560  1.12838E-05 0.31996 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  6.98253E-03 0.24624  1.16130E-04 1.00000  2.92190E-04 0.59009  7.50658E-04 0.58063  4.78720E-03 0.29390  8.32703E-04 0.54257  2.03652E-04 0.75583 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  1.04562E+00 0.40281  1.24906E-02 0.0E+00  3.18241E-02 0.0E+00  1.13313E-01 0.01419  3.22641E-01 0.00923  1.33984E+00 0.00646  8.63638E+00 0.0E+00 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.48085E-03 0.23995  7.92079E-05 1.00000  3.38999E-04 0.64747  8.74403E-04 0.51056  4.05490E-03 0.29806  9.66931E-04 0.57035  1.66411E-04 0.79492 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  9.51688E-01 0.41044  1.24906E-02 0.0E+00  3.18241E-02 0.0E+00  1.13313E-01 0.01419  3.22641E-01 0.00923  1.33984E+00 0.00646  8.63638E+00 0.0E+00 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -3.22243E+02 0.23526 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.18654E-05 0.00746 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.28590E-05 0.00491 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.61686E-03 0.05581 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -3.06232E+02 0.05809 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.56980E-07 0.00491 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  3.45293E-06 0.00428  3.45082E-06 0.00433  3.84699E-06 0.05573 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.76143E-05 0.00607  2.75689E-05 0.00618  3.28505E-05 0.08707 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.97233E-01 0.00418  5.96592E-01 0.00427  8.03351E-01 0.08118 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.05593E+01 0.26282 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.89489E+01 0.00227  3.06815E+01 0.00387 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  8.69393E+03 0.04631  3.32917E+04 0.02612  7.13902E+04 0.00055  8.02122E+04 0.00366  7.55150E+04 0.01069  8.23582E+04 0.00605  5.56892E+04 0.00569  5.03197E+04 0.00677  3.85127E+04 0.01478  3.07836E+04 0.00170  2.73911E+04 0.00595  2.35657E+04 0.00282  2.20376E+04 0.00069  2.11146E+04 0.01160  2.02156E+04 0.00480  1.75416E+04 0.01038  1.73929E+04 0.00818  1.69989E+04 0.00192  1.63369E+04 0.00380  3.25211E+04 0.00403  3.07634E+04 0.00475  2.15313E+04 0.00046  1.39142E+04 0.00453  1.60102E+04 0.00019  1.48573E+04 0.00987  1.32928E+04 0.00013  2.20037E+04 0.00951  5.06679E+03 0.00571  5.99251E+03 0.02026  5.55462E+03 0.00751  3.32305E+03 0.04885  5.67176E+03 0.01926  3.90727E+03 0.02445  3.23207E+03 0.00052  6.17396E+02 0.05241  6.14903E+02 0.00531  6.30738E+02 0.02835  6.63568E+02 0.00296  5.94317E+02 0.06799  6.12098E+02 0.04790  6.08284E+02 0.00260  5.92713E+02 0.00696  1.13778E+03 0.03080  1.84547E+03 0.01765  2.26965E+03 0.01045  6.09260E+03 0.00168  6.24751E+03 0.00638  6.38071E+03 0.00237  4.05559E+03 0.01019  2.85458E+03 0.01737  2.11537E+03 0.00202  2.52290E+03 0.02372  4.55637E+03 0.01974  5.74160E+03 5.8E-05  1.06071E+04 0.01086  1.47508E+04 0.00317  2.07580E+04 0.01179  1.26243E+04 0.01538  8.84350E+03 0.02502  6.33902E+03 0.04002  5.56280E+03 0.01847  5.37045E+03 0.02908  4.59093E+03 0.02787  3.04282E+03 0.02366  2.84299E+03 0.01629  2.56409E+03 0.00924  2.18303E+03 0.00247  1.69721E+03 0.00428  1.07167E+03 0.02012  3.69908E+02 0.00941 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.04599E+00 0.00236 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  4.60949E+01 0.00238  6.87401E+00 0.00827 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.46364E-01 0.00045  1.21279E+00 0.00220 ];
INF_CAPT                  (idx, [1:   4]) = [  5.87001E-03 0.00655  4.44883E-02 0.00897 ];
INF_ABS                   (idx, [1:   4]) = [  8.71441E-03 0.00416  8.70966E-02 0.00957 ];
INF_FISS                  (idx, [1:   4]) = [  2.84440E-03 0.00078  4.26083E-02 0.01020 ];
INF_NSF                   (idx, [1:   4]) = [  7.17603E-03 1.2E-05  1.03824E-01 0.01020 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.52286E+00 0.00077  2.43670E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03274E+02 4.0E-05  2.02270E+02 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.43411E-08 0.00355  2.38794E-06 0.00122 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.37548E-01 0.00050  1.12643E+00 0.00353 ];
INF_SCATT1                (idx, [1:   4]) = [  1.93046E-01 0.00183  3.09440E-01 0.00172 ];
INF_SCATT2                (idx, [1:   4]) = [  7.65594E-02 0.00279  7.72132E-02 0.00623 ];
INF_SCATT3                (idx, [1:   4]) = [  6.09694E-03 0.01705  2.41680E-02 0.00674 ];
INF_SCATT4                (idx, [1:   4]) = [ -7.60604E-03 0.00303 -5.53690E-03 0.12515 ];
INF_SCATT5                (idx, [1:   4]) = [  4.32251E-04 0.28425  5.11821E-03 0.11099 ];
INF_SCATT6                (idx, [1:   4]) = [  4.05934E-03 0.00035 -1.04468E-02 0.02383 ];
INF_SCATT7                (idx, [1:   4]) = [  9.08177E-04 0.07389  1.25037E-03 0.13277 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.37580E-01 0.00049  1.12643E+00 0.00353 ];
INF_SCATTP1               (idx, [1:   4]) = [  1.93043E-01 0.00183  3.09440E-01 0.00172 ];
INF_SCATTP2               (idx, [1:   4]) = [  7.65573E-02 0.00281  7.72132E-02 0.00623 ];
INF_SCATTP3               (idx, [1:   4]) = [  6.09816E-03 0.01745  2.41680E-02 0.00674 ];
INF_SCATTP4               (idx, [1:   4]) = [ -7.60632E-03 0.00293 -5.53690E-03 0.12515 ];
INF_SCATTP5               (idx, [1:   4]) = [  4.32947E-04 0.28495  5.11821E-03 0.11099 ];
INF_SCATTP6               (idx, [1:   4]) = [  4.05955E-03 0.00024 -1.04468E-02 0.02383 ];
INF_SCATTP7               (idx, [1:   4]) = [  9.06747E-04 0.07478  1.25037E-03 0.13277 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.88908E-01 0.00238  7.88313E-01 0.00253 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.76453E+00 0.00238  4.22846E-01 0.00253 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  8.68231E-03 0.00371  8.70966E-02 0.00957 ];
INF_REMXS                 (idx, [1:   4]) = [  2.19325E-02 0.00254  8.79689E-02 0.01625 ];

% Poison cross sections:

INF_I135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_YIELD          (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_I135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_MICRO_ABS      (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  4.24432E-01 0.00034  1.31166E-02 0.00561  1.60238E-03 0.07383  1.12482E+00 0.00364 ];
INF_S1                    (idx, [1:   8]) = [  1.89230E-01 0.00174  3.81681E-03 0.00629  6.37102E-04 0.04260  3.08803E-01 0.00164 ];
INF_S2                    (idx, [1:   8]) = [  7.77108E-02 0.00238 -1.15134E-03 0.02475  3.86585E-04 0.05060  7.68266E-02 0.00652 ];
INF_S3                    (idx, [1:   8]) = [  7.48162E-03 0.01710 -1.38468E-03 0.01735  1.40664E-04 0.08897  2.40273E-02 0.00730 ];
INF_S4                    (idx, [1:   8]) = [ -7.16954E-03 0.00639 -4.36497E-04 0.05215 -4.33555E-05 0.32247 -5.49354E-03 0.12868 ];
INF_S5                    (idx, [1:   8]) = [  3.68384E-04 0.41913  6.38672E-05 0.49373 -8.74883E-05 0.01305  5.20570E-03 0.10890 ];
INF_S6                    (idx, [1:   8]) = [  4.15410E-03 0.00054 -9.47649E-05 0.00851 -5.03673E-05 0.10621 -1.03964E-02 0.02446 ];
INF_S7                    (idx, [1:   8]) = [  1.06427E-03 0.04344 -1.56095E-04 0.13372 -4.50402E-05 0.43169  1.29541E-03 0.14317 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  4.24464E-01 0.00033  1.31166E-02 0.00561  1.60238E-03 0.07383  1.12482E+00 0.00364 ];
INF_SP1                   (idx, [1:   8]) = [  1.89226E-01 0.00174  3.81681E-03 0.00629  6.37102E-04 0.04260  3.08803E-01 0.00164 ];
INF_SP2                   (idx, [1:   8]) = [  7.77087E-02 0.00240 -1.15134E-03 0.02475  3.86585E-04 0.05060  7.68266E-02 0.00652 ];
INF_SP3                   (idx, [1:   8]) = [  7.48284E-03 0.01743 -1.38468E-03 0.01735  1.40664E-04 0.08897  2.40273E-02 0.00730 ];
INF_SP4                   (idx, [1:   8]) = [ -7.16982E-03 0.00628 -4.36497E-04 0.05215 -4.33555E-05 0.32247 -5.49354E-03 0.12868 ];
INF_SP5                   (idx, [1:   8]) = [  3.69079E-04 0.41970  6.38672E-05 0.49373 -8.74883E-05 0.01305  5.20570E-03 0.10890 ];
INF_SP6                   (idx, [1:   8]) = [  4.15431E-03 0.00042 -9.47649E-05 0.00851 -5.03673E-05 0.10621 -1.03964E-02 0.02446 ];
INF_SP7                   (idx, [1:   8]) = [  1.06284E-03 0.04416 -1.56095E-04 0.13372 -4.50402E-05 0.43169  1.29541E-03 0.14317 ];

% Micro-group spectrum:

B1_MICRO_FLX              (idx, [1: 140]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Integral parameters:

B1_KINF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_KEFF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_B2                     (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_ERR                    (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Critical spectra in infinite geometry:

B1_FLX                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS_FLX               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

B1_TOT                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CAPT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABS                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NUBAR                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_KAPPA                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INVV                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering cross sections:

B1_SCATT0                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT1                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT2                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT3                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT4                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT5                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT6                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT7                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering production cross sections:

B1_SCATTP0                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP1                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP2                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP3                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP4                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP5                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP6                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP7                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Diffusion parameters:

B1_TRANSPXS               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reduced absoption and removal:

B1_RABSXS                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Poison cross sections:

B1_I135_YIELD             (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_I135_MICRO_ABS         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

B1_CHIT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHIP                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHID                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

B1_S0                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S1                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S2                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S3                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S4                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S5                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S6                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S7                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering production matrixes:

B1_SP0                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP1                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP2                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP3                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP4                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP5                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP6                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP7                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Additional diffusion parameters:

CMM_TRANSPXS              (idx, [1:   4]) = [  1.96135E-01 0.00395  6.07386E-01 0.04515 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.95400E-01 0.01220  6.50795E-01 0.11787 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.96561E-01 0.00569  5.84789E-01 0.00765 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.96480E-01 0.00528  5.95056E-01 0.01588 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.69954E+00 0.00395  5.49921E-01 0.04515 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.70616E+00 0.01220  5.19410E-01 0.11787 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.69588E+00 0.00569  5.70040E-01 0.00765 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.69657E+00 0.00528  5.60312E-01 0.01588 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  7.62745E-03 0.07592  1.84248E-04 0.49035  1.14646E-03 0.20405  1.20788E-03 0.22169  3.45117E-03 0.10925  1.13207E-03 0.18412  5.05625E-04 0.35405 ];
LAMBDA                    (idx, [1:  14]) = [  8.83572E-01 0.19655  1.24906E-02 0.0E+00  3.17288E-02 0.00209  1.10395E-01 0.00323  3.19909E-01 0.00245  1.34783E+00 0.00156  8.89745E+00 0.01691 ];

