

% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.29' ;
COMPILE_DATE              (idx, [1: 20])  = 'Jan  4 2018 17:22:46' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1:  7])  = 'pwr pin' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1:  6])  = 'pwrPin' ;
WORKING_DIRECTORY         (idx, [1: 49])  = '/home/ajohnson400/research/gpt-dep/testing/depmtx' ;
HOSTNAME                  (idx, [1: 14])  = 'ME04L0358GRD04' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i7-6700T CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 194.0 ;
START_DATE                (idx, [1: 24])  = 'Mon Feb 19 15:39:23 2018' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Mon Feb 19 15:39:40 2018' ;

% Run parameters:

POP                       (idx, 1)        = 1000 ;
CYCLES                    (idx, 1)        = 100 ;
SKIP                      (idx, 1)        = 50 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1519072763 ;
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
SPECTRUM_COLLAPSE         (idx, 1)        = 1 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 1 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
SHARE_BUF_ARRAY           (idx, 1)        = 1 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 22])  = '/xs/sss_endfb7u.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.15953E-02 0.00723  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.88405E-01 8.5E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  7.23048E-01 0.00042  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  7.23672E-01 0.00041  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.73712E+00 0.00148  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.53320E+01 0.00161  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.53320E+01 0.00161  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  9.67330E+00 0.00214  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  3.30730E-01 0.00745  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 100 ;
SOURCE_POPULATION         (idx, 1)        = 100108 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  1.00108E+03 0.00613 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  1.00108E+03 0.00613 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.82078E-01 ;
RUNNING_TIME              (idx, 1)        =  2.82067E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.04367E-01  1.04367E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.99999E-04  1.99999E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.77500E-01  1.77500E-01  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  2.82050E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 1.00004 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  9.99883E-01 0.00045 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  6.29638E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 15935.20 ;
ALLOC_MEMSIZE             (idx, 1)        = 1442.06;
MEMSIZE                   (idx, 1)        = 1400.35;
XS_MEMSIZE                (idx, 1)        = 1369.64;
MAT_MEMSIZE               (idx, 1)        = 23.39;
RES_MEMSIZE               (idx, 1)        = 0.74;
MISC_MEMSIZE              (idx, 1)        = 6.59;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 41.70;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 2 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  5.00000E-05 ;
NEUTRON_ERG_NE            (idx, 1)        = 177481 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 97 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 116 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 116 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 3132 ;
TOT_TRANSMU_REA           (idx, 1)        = 937 ;

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

TOT_ACTIVITY              (idx, 1)        =  0.00000E+00 ;
TOT_DECAY_HEAT            (idx, 1)        =  0.00000E+00 ;
TOT_SF_RATE               (idx, 1)        =  0.00000E+00 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  0.00000E+00 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  0.00000E+00 ;
INGESTION_TOXICITY        (idx, 1)        =  0.00000E+00 ;
ACTINIDE_INH_TOX          (idx, 1)        =  0.00000E+00 ;
ACTINIDE_ING_TOX          (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_INH_TOX   (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_ING_TOX   (idx, 1)        =  0.00000E+00 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
PHOTON_DECAY_SOURCE       (idx, 1)        =  0.00000E+00 ;
NEUTRON_DECAY_SOURCE      (idx, 1)        =  0.00000E+00 ;
ALPHA_DECAY_SOURCE        (idx, 1)        =  0.00000E+00 ;
BETA_DECAY_SOURCE         (idx, 1)        =  0.00000E+00 ;

% Normaliation coefficient:

NORM_COEF                 (idx, [1:   4]) = [  6.25918E+13 0.00277  0.00000E+00 0.0E+00 ];

% Parameters for burnup calculation:

BURN_MATERIALS            (idx, 1)        = 1 ;
BURN_MODE                 (idx, 1)        = 2 ;
BURN_STEP                 (idx, 1)        = 0 ;
BURNUP                     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BURN_DAYS                 (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.28010E-01 0.00780 ];
U235_FISS                 (idx, [1:   4]) = [  2.35298E+16 0.00450  9.29981E-01 0.00137 ];
U238_FISS                 (idx, [1:   4]) = [  1.77447E+15 0.01951  7.00193E-02 0.01818 ];
U235_CAPT                 (idx, [1:   4]) = [  5.70110E+15 0.01159  1.52432E-01 0.01047 ];
U238_CAPT                 (idx, [1:   4]) = [  1.54152E+16 0.00704  4.12161E-01 0.00497 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS       (idx, [1:  2])  = [ 100108 1.00000E+05 ];
BALA_SRC_NEUTRON_NXN        (idx, [1:  2])  = [ 0 1.61049E+02 ];
BALA_SRC_NEUTRON_VR         (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT        (idx, [1:  2])  = [ 100108 1.00161E+05 ];

BALA_LOSS_NEUTRON_CAPT       (idx, [1:  2])  = [ 59692 5.97248E+04 ];
BALA_LOSS_NEUTRON_FISS       (idx, [1:  2])  = [ 40416 4.04362E+04 ];
BALA_LOSS_NEUTRON_LEAK       (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT        (idx, [1:  2])  = [ 100108 1.00161E+05 ];

BALA_NEUTRON_DIFF            (idx, [1:  2])  = [ 0 -1.60071E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   6]) = [  8.18837E+05 0.0E+00  8.18837E+05 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_POWDENS               (idx, [1:   6]) = [  1.00000E+02 0.0E+00  1.00000E+02 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   6]) = [  6.21302E+16 7.1E-05  6.21302E+16 7.1E-05  0.00000E+00 0.0E+00 ];
TOT_FISSRATE              (idx, [1:   6]) = [  2.52261E+16 8.7E-06  2.52261E+16 8.7E-06  0.00000E+00 0.0E+00 ];
TOT_CAPTRATE              (idx, [1:   6]) = [  3.75120E+16 0.00242  3.52748E+16 0.00252  2.23713E+15 0.00418 ];
TOT_ABSRATE               (idx, [1:   6]) = [  6.27381E+16 0.00145  6.05010E+16 0.00147  2.23713E+15 0.00418 ];
TOT_SRCRATE               (idx, [1:   6]) = [  6.25918E+16 0.00277  6.25918E+16 0.00277  0.00000E+00 0.0E+00 ];
TOT_FLUX                  (idx, [1:   6]) = [  2.76567E+18 0.00231  9.15392E+17 0.00263  1.85028E+18 0.00242 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  6.27381E+16 0.00145 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.58762E+18 0.00207 ];
INI_FMASS                 (idx, 1)        =  8.18837E-03 ;
TOT_FMASS                 (idx, 1)        =  8.18837E-03 ;
INI_BURN_FMASS            (idx, 1)        =  8.18837E-03 ;
TOT_BURN_FMASS            (idx, 1)        =  8.18837E-03 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46293E+00 7.8E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02598E+02 8.7E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  9.95003E-01 0.00411  9.88678E-01 0.00423  7.21837E-03 0.05562 ];
IMP_KEFF                  (idx, [1:   2]) = [  9.91938E-01 0.00145 ];
COL_KEFF                  (idx, [1:   2]) = [  9.93385E-01 0.00279 ];
ABS_KEFF                  (idx, [1:   2]) = [  9.91938E-01 0.00145 ];
ABS_KINF                  (idx, [1:   2]) = [  9.91938E-01 0.00145 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.65383E+01 0.00140 ];
IMP_ALF                   (idx, [1:   2]) = [  1.65378E+01 0.00061 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.34947E-06 0.02353 ];
IMP_EALF                  (idx, [1:   2]) = [  1.32106E-06 0.01004 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.35560E-01 0.01916 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.35768E-01 0.00646 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  7.07827E-03 0.03535  1.95297E-04 0.23313  1.05266E-03 0.09988  9.71555E-04 0.10194  3.31489E-03 0.05246  1.19878E-03 0.08329  3.45080E-04 0.18532 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  8.05262E-01 0.08896  2.12343E-03 0.22207  1.99433E-02 0.07704  6.86603E-02 0.07873  3.11802E-01 0.01780  1.02108E+00 0.05649  2.28574E+00 0.16978 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  7.11548E-03 0.04412  2.56830E-04 0.29203  1.07908E-03 0.13678  1.05453E-03 0.13979  3.22121E-03 0.07295  1.15765E-03 0.11129  3.46174E-04 0.22431 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  7.98255E-01 0.10273  1.24908E-02 1.7E-05  3.16437E-02 0.00176  1.10814E-01 0.00279  3.21275E-01 0.00231  1.34294E+00 0.00131  8.78913E+00 0.00909 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.44347E-05 0.00812  1.44262E-05 0.00806  1.48284E-05 0.11669 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  1.43397E-05 0.00715  1.43315E-05 0.00710  1.47785E-05 0.11947 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  7.30903E-03 0.05692  1.50064E-04 0.36985  1.14362E-03 0.14910  1.07187E-03 0.16575  3.29586E-03 0.08798  1.27220E-03 0.11684  3.75423E-04 0.26041 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  9.08535E-01 0.15277  1.24911E-02 4.2E-05  3.16403E-02 0.00240  1.10905E-01 0.00421  3.21594E-01 0.00301  1.34232E+00 0.00176  8.92409E+00 0.01712 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.45005E-05 0.01782  1.44653E-05 0.01774  6.69851E-06 0.20181 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.44054E-05 0.01744  1.43698E-05 0.01732  6.74257E-06 0.20281 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  6.81677E-03 0.19262  4.35444E-05 1.00000  1.22724E-03 0.39033  1.73035E-03 0.45604  2.46987E-03 0.35971  1.09858E-03 0.40210  2.47181E-04 0.67107 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  8.46766E-01 0.31621  1.24906E-02 0.0E+00  3.16497E-02 0.00551  1.11807E-01 0.01186  3.25152E-01 0.01070  1.33984E+00 0.00431  9.08393E+00 0.04927 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  7.00591E-03 0.19192  1.24352E-04 1.00000  1.32038E-03 0.37979  1.62989E-03 0.45059  2.53292E-03 0.36014  1.13212E-03 0.41908  2.66235E-04 0.64677 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  8.52023E-01 0.31930  1.24906E-02 0.0E+00  3.16497E-02 0.00551  1.11817E-01 0.01185  3.25152E-01 0.01070  1.33984E+00 0.00431  9.08393E+00 0.04927 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -4.80007E+02 0.19080 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.45061E-05 0.00580 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  1.44076E-05 0.00377 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.82314E-03 0.03199 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.72066E+02 0.03297 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  2.87131E-07 0.00332 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  3.19460E-06 0.00312  3.19437E-06 0.00315  3.22972E-06 0.04088 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  1.78186E-05 0.00354  1.78175E-05 0.00353  1.76329E-05 0.06006 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.88897E-01 0.00250  5.88659E-01 0.00256  7.34961E-01 0.07121 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  8.53995E+00 0.08678 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.53320E+01 0.00161  2.66055E+01 0.00223 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  5.98814E+03 0.03204  2.54738E+04 0.00396  5.56739E+04 0.00774  6.89606E+04 0.00435  6.88726E+04 0.00390  6.86491E+04 0.00823  5.00941E+04 0.00613  4.11271E+04 0.00502  3.09051E+04 0.00435  2.75490E+04 0.00958  2.27236E+04 0.00318  2.04900E+04 0.00749  1.89097E+04 0.00458  1.80845E+04 0.00495  1.77249E+04 0.00606  1.51110E+04 0.00815  1.47714E+04 0.00915  1.45613E+04 0.00900  1.44235E+04 0.00346  2.81492E+04 0.00745  2.67667E+04 0.00402  1.90413E+04 0.00525  1.23002E+04 0.00543  1.38967E+04 0.00808  1.31336E+04 0.00823  1.19198E+04 0.00647  1.89711E+04 0.00615  4.48940E+03 0.01010  5.48311E+03 0.01125  4.99238E+03 0.01133  2.93029E+03 0.00539  5.09418E+03 0.00884  3.44164E+03 0.00841  2.87233E+03 0.01596  5.52433E+02 0.02548  5.42384E+02 0.03597  5.27664E+02 0.02666  5.84317E+02 0.04854  5.89489E+02 0.03272  5.67638E+02 0.00919  5.80933E+02 0.02320  5.11398E+02 0.03642  1.01756E+03 0.02876  1.64873E+03 0.03031  2.12306E+03 0.02105  5.55097E+03 0.01866  5.63969E+03 0.00479  5.91573E+03 0.01452  3.69646E+03 0.00658  2.57869E+03 0.00987  1.87891E+03 0.00979  2.09695E+03 0.00760  3.72985E+03 0.01165  4.60170E+03 0.01075  8.08186E+03 0.00976  1.07775E+04 0.01321  1.39921E+04 0.00321  8.00546E+03 0.00959  5.34091E+03 0.01048  3.65731E+03 0.01204  3.15607E+03 0.00915  2.98708E+03 0.00578  2.42131E+03 0.01521  1.60073E+03 0.00668  1.44822E+03 0.01338  1.28403E+03 0.00879  1.08511E+03 0.01466  8.23442E+02 0.01580  5.45697E+02 0.01171  1.98750E+02 0.03990 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  9.93385E-01 0.00254 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.46724E+18 0.00115  2.98999E+17 0.00311 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.96553E-01 0.00044  1.21388E+00 0.00080 ];
INF_CAPT                  (idx, [1:   4]) = [  7.48420E-03 0.00597  6.37459E-02 0.00230 ];
INF_ABS                   (idx, [1:   4]) = [  1.05040E-02 0.00482  1.23260E-01 0.00202 ];
INF_FISS                  (idx, [1:   4]) = [  3.01983E-03 0.00259  5.95139E-02 0.00182 ];
INF_NSF                   (idx, [1:   4]) = [  7.62666E-03 0.00247  1.45018E-01 0.00182 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.52553E+00 0.00036  2.43670E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03382E+02 4.0E-05  2.02270E+02 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.66031E-08 0.00291  2.18946E-06 0.00116 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.86070E-01 0.00041  1.09070E+00 0.00121 ];
INF_SCATT1                (idx, [1:   4]) = [  2.24971E-01 0.00052  3.09829E-01 0.00155 ];
INF_SCATT2                (idx, [1:   4]) = [  8.90623E-02 0.00132  8.18680E-02 0.00622 ];
INF_SCATT3                (idx, [1:   4]) = [  6.87009E-03 0.01816  2.51626E-02 0.02423 ];
INF_SCATT4                (idx, [1:   4]) = [ -8.93762E-03 0.00972 -3.26357E-03 0.11192 ];
INF_SCATT5                (idx, [1:   4]) = [  3.09960E-04 0.23513  4.51145E-03 0.10132 ];
INF_SCATT6                (idx, [1:   4]) = [  4.67651E-03 0.02706 -1.05531E-02 0.03228 ];
INF_SCATT7                (idx, [1:   4]) = [  6.43493E-04 0.09483 -5.14640E-04 0.89413 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.86111E-01 0.00041  1.09070E+00 0.00121 ];
INF_SCATTP1               (idx, [1:   4]) = [  2.24970E-01 0.00052  3.09829E-01 0.00155 ];
INF_SCATTP2               (idx, [1:   4]) = [  8.90618E-02 0.00133  8.18680E-02 0.00622 ];
INF_SCATTP3               (idx, [1:   4]) = [  6.87011E-03 0.01815  2.51626E-02 0.02423 ];
INF_SCATTP4               (idx, [1:   4]) = [ -8.93666E-03 0.00971 -3.26357E-03 0.11192 ];
INF_SCATTP5               (idx, [1:   4]) = [  3.10447E-04 0.23618  4.51145E-03 0.10132 ];
INF_SCATTP6               (idx, [1:   4]) = [  4.67736E-03 0.02706 -1.05531E-02 0.03228 ];
INF_SCATTP7               (idx, [1:   4]) = [  6.43561E-04 0.09525 -5.14640E-04 0.89413 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.12372E-01 0.00125  7.73223E-01 0.00170 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.56958E+00 0.00125  4.31101E-01 0.00170 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.04632E-02 0.00465  1.23260E-01 0.00202 ];
INF_REMXS                 (idx, [1:   4]) = [  2.56370E-02 0.00164  1.25053E-01 0.00368 ];

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

INF_S0                    (idx, [1:   8]) = [  4.70916E-01 0.00043  1.51543E-02 0.00154  1.87383E-03 0.06214  1.08882E+00 0.00125 ];
INF_S1                    (idx, [1:   8]) = [  2.20479E-01 0.00051  4.49252E-03 0.00305  8.88773E-04 0.09185  3.08941E-01 0.00142 ];
INF_S2                    (idx, [1:   8]) = [  9.03697E-02 0.00146 -1.30744E-03 0.01985  4.64303E-04 0.09948  8.14037E-02 0.00642 ];
INF_S3                    (idx, [1:   8]) = [  8.43117E-03 0.01477 -1.56108E-03 0.01002  1.49234E-04 0.17176  2.50133E-02 0.02367 ];
INF_S4                    (idx, [1:   8]) = [ -8.40578E-03 0.01101 -5.31845E-04 0.03512 -7.13575E-06 1.00000 -3.25644E-03 0.11518 ];
INF_S5                    (idx, [1:   8]) = [  3.08437E-04 0.25391  1.52329E-06 1.00000 -8.16540E-05 0.24226  4.59310E-03 0.09945 ];
INF_S6                    (idx, [1:   8]) = [  4.79518E-03 0.02682 -1.18667E-04 0.10542 -9.43965E-05 0.14941 -1.04587E-02 0.03216 ];
INF_S7                    (idx, [1:   8]) = [  7.73529E-04 0.07278 -1.30035E-04 0.18277 -7.38834E-05 0.17833 -4.40756E-04 1.00000 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  4.70957E-01 0.00043  1.51543E-02 0.00154  1.87383E-03 0.06214  1.08882E+00 0.00125 ];
INF_SP1                   (idx, [1:   8]) = [  2.20478E-01 0.00051  4.49252E-03 0.00305  8.88773E-04 0.09185  3.08941E-01 0.00142 ];
INF_SP2                   (idx, [1:   8]) = [  9.03692E-02 0.00147 -1.30744E-03 0.01985  4.64303E-04 0.09948  8.14037E-02 0.00642 ];
INF_SP3                   (idx, [1:   8]) = [  8.43119E-03 0.01476 -1.56108E-03 0.01002  1.49234E-04 0.17176  2.50133E-02 0.02367 ];
INF_SP4                   (idx, [1:   8]) = [ -8.40481E-03 0.01099 -5.31845E-04 0.03512 -7.13575E-06 1.00000 -3.25644E-03 0.11518 ];
INF_SP5                   (idx, [1:   8]) = [  3.08924E-04 0.25449  1.52329E-06 1.00000 -8.16540E-05 0.24226  4.59310E-03 0.09945 ];
INF_SP6                   (idx, [1:   8]) = [  4.79603E-03 0.02683 -1.18667E-04 0.10542 -9.43965E-05 0.14941 -1.04587E-02 0.03216 ];
INF_SP7                   (idx, [1:   8]) = [  7.73597E-04 0.07334 -1.30035E-04 0.18277 -7.38834E-05 0.17833 -4.40756E-04 1.00000 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  2.23062E-01 0.00144  6.55491E-01 0.03837 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  2.24465E-01 0.00461  6.37370E-01 0.02124 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  2.23098E-01 0.00693  6.50628E-01 0.05606 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  2.21719E-01 0.00514  6.86625E-01 0.06044 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.49437E+00 0.00144  5.11474E-01 0.03771 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.48514E+00 0.00461  5.23979E-01 0.02239 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.49440E+00 0.00696  5.18762E-01 0.05572 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.50356E+00 0.00510  4.91682E-01 0.05240 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  7.11548E-03 0.04412  2.56830E-04 0.29203  1.07908E-03 0.13678  1.05453E-03 0.13979  3.22121E-03 0.07295  1.15765E-03 0.11129  3.46174E-04 0.22431 ];
LAMBDA                    (idx, [1:  14]) = [  7.98255E-01 0.10273  1.24908E-02 1.7E-05  3.16437E-02 0.00176  1.10814E-01 0.00279  3.21275E-01 0.00231  1.34294E+00 0.00131  8.78913E+00 0.00909 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.29' ;
COMPILE_DATE              (idx, [1: 20])  = 'Jan  4 2018 17:22:46' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1:  7])  = 'pwr pin' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1:  6])  = 'pwrPin' ;
WORKING_DIRECTORY         (idx, [1: 49])  = '/home/ajohnson400/research/gpt-dep/testing/depmtx' ;
HOSTNAME                  (idx, [1: 14])  = 'ME04L0358GRD04' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i7-6700T CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 194.0 ;
START_DATE                (idx, [1: 24])  = 'Mon Feb 19 15:39:23 2018' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Mon Feb 19 15:39:53 2018' ;

% Run parameters:

POP                       (idx, 1)        = 1000 ;
CYCLES                    (idx, 1)        = 100 ;
SKIP                      (idx, 1)        = 50 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1519072763 ;
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
SPECTRUM_COLLAPSE         (idx, 1)        = 1 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 1 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
SHARE_BUF_ARRAY           (idx, 1)        = 1 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 22])  = '/xs/sss_endfb7u.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.14466E-02 0.00697  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.88553E-01 8.1E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  6.86141E-01 0.00046  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  6.86642E-01 0.00046  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.79372E+00 0.00201  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  3.31516E+01 0.00190  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  3.31516E+01 0.00190  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.51308E+01 0.00255  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  4.81151E-01 0.00751  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 100 ;
SOURCE_POPULATION         (idx, 1)        = 101020 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  1.01020E+03 0.01515 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  1.01020E+03 0.01515 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  4.94889E-01 ;
RUNNING_TIME              (idx, 1)        =  4.94883E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.04367E-01  1.04367E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  6.50001E-04  4.50001E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  3.87967E-01  2.10467E-01  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  1.86667E-03  1.86667E-03 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  2.54313E-10  2.54313E-10 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.94867E-01  4.94867E-01 ];
CPU_USAGE                 (idx, 1)        = 1.00001 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  9.99853E-01 0.00048 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  7.86684E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 15935.20 ;
ALLOC_MEMSIZE             (idx, 1)        = 1442.06;
MEMSIZE                   (idx, 1)        = 1400.35;
XS_MEMSIZE                (idx, 1)        = 1369.64;
MAT_MEMSIZE               (idx, 1)        = 23.39;
RES_MEMSIZE               (idx, 1)        = 0.74;
MISC_MEMSIZE              (idx, 1)        = 6.59;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 41.70;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 2 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  5.00000E-05 ;
NEUTRON_ERG_NE            (idx, 1)        = 177481 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 97 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 116 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 116 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 3132 ;
TOT_TRANSMU_REA           (idx, 1)        = 937 ;

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

TOT_ACTIVITY              (idx, 1)        =  0.00000E+00 ;
TOT_DECAY_HEAT            (idx, 1)        =  0.00000E+00 ;
TOT_SF_RATE               (idx, 1)        =  0.00000E+00 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  0.00000E+00 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  0.00000E+00 ;
INGESTION_TOXICITY        (idx, 1)        =  0.00000E+00 ;
ACTINIDE_INH_TOX          (idx, 1)        =  0.00000E+00 ;
ACTINIDE_ING_TOX          (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_INH_TOX   (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_ING_TOX   (idx, 1)        =  0.00000E+00 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
PHOTON_DECAY_SOURCE       (idx, 1)        =  0.00000E+00 ;
NEUTRON_DECAY_SOURCE      (idx, 1)        =  0.00000E+00 ;
ALPHA_DECAY_SOURCE        (idx, 1)        =  0.00000E+00 ;
BETA_DECAY_SOURCE         (idx, 1)        =  0.00000E+00 ;

% Normaliation coefficient:

NORM_COEF                 (idx, [1:   4]) = [  3.56830E+14 0.00332  0.00000E+00 0.0E+00 ];

% Parameters for burnup calculation:

BURN_MATERIALS            (idx, 1)        = 1 ;
BURN_MODE                 (idx, 1)        = 2 ;
BURN_STEP                 (idx, 1)        = 1 ;
BURNUP                     (idx, [1:  2])  = [  5.00000E+02  5.00260E+02 ];
BURN_DAYS                 (idx, 1)        =  5.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
U238_FISS                 (idx, [1:   4]) = [  7.00334E+15 0.01958  2.62627E-01 0.01846 ];
U238_CAPT                 (idx, [1:   4]) = [  8.58499E+16 0.00698  2.59629E-01 0.00567 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS       (idx, [1:  2])  = [ 101020 1.00000E+05 ];
BALA_SRC_NEUTRON_NXN        (idx, [1:  2])  = [ 0 1.48693E+02 ];
BALA_SRC_NEUTRON_VR         (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT        (idx, [1:  2])  = [ 101020 1.00149E+05 ];

BALA_LOSS_NEUTRON_CAPT       (idx, [1:  2])  = [ 93449 9.26465E+04 ];
BALA_LOSS_NEUTRON_FISS       (idx, [1:  2])  = [ 7571 7.50215E+03 ];
BALA_LOSS_NEUTRON_LEAK       (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT        (idx, [1:  2])  = [ 101020 1.00149E+05 ];

BALA_NEUTRON_DIFF            (idx, [1:  2])  = [ 0 -5.82077E-11 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   6]) = [  8.18837E+05 0.0E+00  8.18837E+05 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_POWDENS               (idx, [1:   6]) = [  1.00000E+02 0.0E+00  1.00000E+02 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   6]) = [  6.46771E+16 0.00025  6.46771E+16 0.00025  0.00000E+00 0.0E+00 ];
TOT_FISSRATE              (idx, [1:   6]) = [  2.64470E+16 0.00013  2.64470E+16 0.00013  0.00000E+00 0.0E+00 ];
TOT_CAPTRATE              (idx, [1:   6]) = [  3.30188E+17 0.00253  3.05261E+17 0.00263  2.49272E+16 0.00323 ];
TOT_ABSRATE               (idx, [1:   6]) = [  3.56635E+17 0.00235  3.31708E+17 0.00242  2.49272E+16 0.00323 ];
TOT_SRCRATE               (idx, [1:   6]) = [  3.56830E+17 0.00332  3.56830E+17 0.00332  0.00000E+00 0.0E+00 ];
TOT_FLUX                  (idx, [1:   6]) = [  1.81052E+19 0.00264  5.98875E+18 0.00289  1.21164E+19 0.00275 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  3.56635E+17 0.00235 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.18412E+19 0.00242 ];
INI_FMASS                 (idx, 1)        =  8.18837E-03 ;
TOT_FMASS                 (idx, 1)        =  6.27956E-03 ;
INI_BURN_FMASS            (idx, 1)        =  8.18837E-03 ;
TOT_BURN_FMASS            (idx, 1)        =  6.27956E-03 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.44555E+00 0.00035 ];
FISSE                     (idx, [1:   2]) = [  1.93246E+02 0.00013 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.83604E-01 0.01097  1.81980E-01 0.01105  1.56566E-03 0.10949 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.81729E-01 0.00240 ];
COL_KEFF                  (idx, [1:   2]) = [  1.81451E-01 0.00331 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.81729E-01 0.00240 ];
ABS_KINF                  (idx, [1:   2]) = [  1.81729E-01 0.00240 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.36092E+01 0.00622 ];
IMP_ALF                   (idx, [1:   2]) = [  1.35614E+01 0.00220 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  3.54297E-05 0.10505 ];
IMP_EALF                  (idx, [1:   2]) = [  2.68967E-05 0.02850 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  9.06004E-01 0.01868 ];
IMP_AFGE                  (idx, [1:   2]) = [  8.97320E-01 0.00623 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  8.19004E-02 0.03528  6.96658E-04 0.26281  1.41616E-02 0.06425  1.14726E-02 0.06977  3.75564E-02 0.04325  1.47713E-02 0.06810  3.24177E-03 0.13212 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  7.97915E-01 0.06638  1.62437E-03 0.26000  2.76255E-02 0.03161  9.81742E-02 0.03362  3.28950E-01 0.00114  1.20884E+00 0.03161  4.19314E+00 0.11576 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  1.01167E-02 0.04089  8.20976E-05 0.35790  1.98516E-03 0.08643  1.41986E-03 0.10516  4.72005E-03 0.07155  1.62300E-03 0.09408  2.86509E-04 0.21973 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  6.71899E-01 0.08637  1.24951E-02 1.6E-05  3.03559E-02 0.00014  1.09074E-01 0.00327  3.28731E-01 0.00141  1.32795E+00 0.00048  9.75809E+00 0.00327 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.54427E-04 0.02464  1.53690E-04 0.02453  9.09619E-05 0.18335 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.80538E-05 0.02229  2.79211E-05 0.02218  1.66652E-05 0.18784 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  8.67260E-03 0.11411  1.12652E-04 1.00000  2.01105E-03 0.24589  1.16891E-03 0.32306  4.41395E-03 0.17707  7.30346E-04 0.40150  2.35692E-04 0.71204 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  5.80037E-01 0.33387  1.24958E-02 0.0E+00  3.03549E-02 0.00044  1.08906E-01 0.01220  3.29957E-01 0.00448  1.32644E+00 0.00263  9.76160E+00 0.02227 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.34204E-04 0.06114  1.33911E-04 0.06193  1.49162E-05 0.35957 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.44757E-05 0.06254  2.44251E-05 0.06348  2.77849E-06 0.36113 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  1.35481E-02 0.42140  0.00000E+00 0.0E+00  7.39830E-03 0.69315  1.90623E-04 1.00000  4.25051E-03 0.51622  1.70864E-03 0.93185  0.00000E+00 0.0E+00 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  4.14225E-01 0.34593  0.00000E+00 0.0E+00  3.03798E-02 0.0E+00  1.06897E-01 0.0E+00  3.37987E-01 0.01032  1.33425E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  1.42782E-02 0.41568  0.00000E+00 0.0E+00  7.90217E-03 0.67456  1.10565E-04 1.00000  4.38672E-03 0.51163  1.87879E-03 0.91589  0.00000E+00 0.0E+00 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  4.14225E-01 0.34593  0.00000E+00 0.0E+00  3.03798E-02 0.0E+00  1.06898E-01 0.0E+00  3.37987E-01 0.01032  1.33425E+00 1.5E-08  0.00000E+00 0.0E+00 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.43124E+02 0.42277 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.52854E-04 0.01662 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.77088E-05 0.01182 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  1.12282E-02 0.06865 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -7.40118E+01 0.06793 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  5.62188E-07 0.00306 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  3.19721E-06 0.00314  3.19699E-06 0.00316  3.21381E-06 0.02729 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  4.43181E-05 0.00367  4.43412E-05 0.00375  4.27579E-05 0.03023 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.95479E-01 0.00251  6.39580E-01 0.00414  1.21134E-01 0.04598 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  9.48983E+00 0.05467 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  3.31516E+01 0.00190  3.01486E+01 0.00990 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  6.30303E+03 0.02369  2.61738E+04 0.01190  5.55598E+04 0.01051  7.09799E+04 0.00786  7.04961E+04 0.00796  6.94812E+04 0.00321  5.10063E+04 0.00593  4.17162E+04 0.00435  3.13773E+04 0.00663  2.80946E+04 0.00125  2.31906E+04 0.00378  2.07455E+04 0.00324  1.94142E+04 0.00259  1.86156E+04 0.00913  1.78794E+04 0.00598  1.55837E+04 0.00612  1.53349E+04 0.01054  1.53003E+04 0.01111  1.50513E+04 0.00734  2.89842E+04 0.00530  2.76128E+04 0.00421  1.98131E+04 0.00693  1.25129E+04 0.00935  1.41639E+04 0.00823  1.33556E+04 0.00579  1.19397E+04 0.00596  1.98951E+04 0.00584  4.67989E+03 0.01025  4.74417E+03 0.01017  4.51932E+03 0.01734  2.91205E+03 0.01242  5.03746E+03 0.01246  3.43960E+03 0.02130  2.93902E+03 0.01855  5.42102E+02 0.03011  5.80311E+02 0.02393  5.50190E+02 0.02604  5.76458E+02 0.02580  5.83206E+02 0.01898  5.72497E+02 0.02327  5.85782E+02 0.02646  5.81129E+02 0.02300  1.04087E+03 0.02263  1.65780E+03 0.00516  2.16878E+03 0.01497  5.67002E+03 0.01153  5.92047E+03 0.01451  6.60827E+03 0.00985  4.56031E+03 0.01644  3.49620E+03 0.01460  2.65976E+03 0.00333  3.17168E+03 0.01824  5.97838E+03 0.00701  8.03378E+03 0.00676  1.50783E+04 0.00461  2.31730E+04 0.00425  3.40421E+04 0.00423  2.16206E+04 0.00542  1.53873E+04 0.00702  1.09360E+04 0.00590  9.78677E+03 0.00557  9.66736E+03 0.00298  7.97447E+03 0.00682  5.46185E+03 0.00958  5.18249E+03 0.00722  4.65071E+03 0.00595  3.54121E+03 0.00247  2.26479E+03 0.00934  1.42406E+03 0.01485  5.09308E+02 0.01678 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.81451E-01 0.00368 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  1.43436E+19 0.00287  3.76672E+18 0.00192 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.81875E-01 0.00084  1.30993E+00 0.00058 ];
INF_CAPT                  (idx, [1:   4]) = [  9.37718E-03 0.00188  5.19922E-02 0.00080 ];
INF_ABS                   (idx, [1:   4]) = [  1.01031E-02 0.00156  5.62564E-02 0.00071 ];
INF_FISS                  (idx, [1:   4]) = [  7.25936E-04 0.00341  4.26421E-03 0.00070 ];
INF_NSF                   (idx, [1:   4]) = [  1.93172E-03 0.00336  9.83262E-03 0.00070 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.66101E+00 0.00041  2.30585E+00 3.2E-07 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.01065E+02 0.00014  1.88175E+02 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.58955E-08 0.00288  2.49046E-06 0.00090 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.71769E-01 0.00082  1.25354E+00 0.00067 ];
INF_SCATT1                (idx, [1:   4]) = [  2.22952E-01 0.00166  2.96932E-01 0.00199 ];
INF_SCATT2                (idx, [1:   4]) = [  8.81854E-02 0.00125  7.08938E-02 0.00419 ];
INF_SCATT3                (idx, [1:   4]) = [  6.50222E-03 0.02983  2.11108E-02 0.01360 ];
INF_SCATT4                (idx, [1:   4]) = [ -9.45838E-03 0.01893 -5.85316E-03 0.07535 ];
INF_SCATT5                (idx, [1:   4]) = [  1.51337E-04 0.96490  4.77016E-03 0.09419 ];
INF_SCATT6                (idx, [1:   4]) = [  4.75821E-03 0.02341 -1.21329E-02 0.01175 ];
INF_SCATT7                (idx, [1:   4]) = [  8.80948E-04 0.08897  2.41828E-04 1.00000 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.71806E-01 0.00082  1.25354E+00 0.00067 ];
INF_SCATTP1               (idx, [1:   4]) = [  2.22953E-01 0.00166  2.96932E-01 0.00199 ];
INF_SCATTP2               (idx, [1:   4]) = [  8.81867E-02 0.00125  7.08938E-02 0.00419 ];
INF_SCATTP3               (idx, [1:   4]) = [  6.50545E-03 0.02981  2.11108E-02 0.01360 ];
INF_SCATTP4               (idx, [1:   4]) = [ -9.45481E-03 0.01894 -5.85316E-03 0.07535 ];
INF_SCATTP5               (idx, [1:   4]) = [  1.51123E-04 0.96375  4.77016E-03 0.09419 ];
INF_SCATTP6               (idx, [1:   4]) = [  4.75981E-03 0.02338 -1.21329E-02 0.01175 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.80556E-04 0.08762  2.41828E-04 1.00000 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.00276E-01 0.00125  8.47607E-01 0.00091 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.66438E+00 0.00125  3.93265E-01 0.00091 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.00661E-02 0.00176  5.62564E-02 0.00071 ];
INF_REMXS                 (idx, [1:   4]) = [  2.51680E-02 0.00180  5.73546E-02 0.00341 ];

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

INF_S0                    (idx, [1:   8]) = [  4.56707E-01 0.00080  1.50615E-02 0.00159  9.67134E-04 0.05281  1.25257E+00 0.00069 ];
INF_S1                    (idx, [1:   8]) = [  2.18535E-01 0.00169  4.41745E-03 0.00603  4.36479E-04 0.05000  2.96495E-01 0.00193 ];
INF_S2                    (idx, [1:   8]) = [  8.95477E-02 0.00112 -1.36224E-03 0.01257  2.36204E-04 0.07802  7.06576E-02 0.00428 ];
INF_S3                    (idx, [1:   8]) = [  8.03229E-03 0.02259 -1.53007E-03 0.00885  9.05341E-05 0.10207  2.10203E-02 0.01374 ];
INF_S4                    (idx, [1:   8]) = [ -8.98757E-03 0.02167 -4.70810E-04 0.04236  1.69256E-05 0.59293 -5.87008E-03 0.07669 ];
INF_S5                    (idx, [1:   8]) = [  1.28288E-04 1.00000  2.30493E-05 0.69916 -3.38943E-05 0.35176  4.80405E-03 0.09544 ];
INF_S6                    (idx, [1:   8]) = [  4.88333E-03 0.02321 -1.25119E-04 0.05871 -4.13460E-05 0.11332 -1.20915E-02 0.01181 ];
INF_S7                    (idx, [1:   8]) = [  1.02839E-03 0.06609 -1.47441E-04 0.17905 -2.70652E-05 0.19138  2.68893E-04 0.95508 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  4.56744E-01 0.00080  1.50615E-02 0.00159  9.67134E-04 0.05281  1.25257E+00 0.00069 ];
INF_SP1                   (idx, [1:   8]) = [  2.18536E-01 0.00169  4.41745E-03 0.00603  4.36479E-04 0.05000  2.96495E-01 0.00193 ];
INF_SP2                   (idx, [1:   8]) = [  8.95490E-02 0.00111 -1.36224E-03 0.01257  2.36204E-04 0.07802  7.06576E-02 0.00428 ];
INF_SP3                   (idx, [1:   8]) = [  8.03553E-03 0.02258 -1.53007E-03 0.00885  9.05341E-05 0.10207  2.10203E-02 0.01374 ];
INF_SP4                   (idx, [1:   8]) = [ -8.98400E-03 0.02168 -4.70810E-04 0.04236  1.69256E-05 0.59293 -5.87008E-03 0.07669 ];
INF_SP5                   (idx, [1:   8]) = [  1.28073E-04 1.00000  2.30493E-05 0.69916 -3.38943E-05 0.35176  4.80405E-03 0.09544 ];
INF_SP6                   (idx, [1:   8]) = [  4.88493E-03 0.02318 -1.25119E-04 0.05871 -4.13460E-05 0.11332 -1.20915E-02 0.01181 ];
INF_SP7                   (idx, [1:   8]) = [  1.02800E-03 0.06518 -1.47441E-04 0.17905 -2.70652E-05 0.19138  2.68893E-04 0.95508 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  2.11125E-01 0.00395  8.06149E-01 0.01690 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  2.11324E-01 0.00560  8.26659E-01 0.01827 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  2.11702E-01 0.00634  7.87061E-01 0.02010 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  2.10418E-01 0.00717  8.08093E-01 0.02892 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.57894E+00 0.00391  4.13959E-01 0.01683 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.57755E+00 0.00560  4.03774E-01 0.01848 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.57480E+00 0.00630  4.24209E-01 0.02031 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.58448E+00 0.00721  4.13894E-01 0.02930 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  1.01167E-02 0.04089  8.20976E-05 0.35790  1.98516E-03 0.08643  1.41986E-03 0.10516  4.72005E-03 0.07155  1.62300E-03 0.09408  2.86509E-04 0.21973 ];
LAMBDA                    (idx, [1:  14]) = [  6.71899E-01 0.08637  1.24951E-02 1.6E-05  3.03559E-02 0.00014  1.09074E-01 0.00327  3.28731E-01 0.00141  1.32795E+00 0.00048  9.75809E+00 0.00327 ];

