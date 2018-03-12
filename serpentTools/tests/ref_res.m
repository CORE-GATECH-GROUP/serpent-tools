
% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98270 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '310' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  1.27573E+15 0.00433  6.84692E+14 0.00536  5.91036E+14 0.00600 ];
LEAK                      (idx, [1:   6]) = [  5.45966E+13 0.00428  3.57539E+13 0.00532  1.88426E+13 0.00752 ];
TOTXS                     (idx, [1:   6]) = [  6.11642E-01 0.00172  4.52762E-01 0.00170  7.96315E-01 0.00170 ];
FISSXS                    (idx, [1:   6]) = [  1.53760E-04 0.01206  2.85622E-04 0.01139  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  1.90509E-02 0.00471  6.12959E-03 0.00756  3.40358E-02 0.00402 ];
ABSXS                     (idx, [1:   6]) = [  1.92047E-02 0.00465  6.41521E-03 0.00716  3.40358E-02 0.00402 ];
RABSXS                    (idx, [1:   6]) = [  1.91460E-02 0.00467  6.30550E-03 0.00736  3.40358E-02 0.00402 ];
ELAXS                     (idx, [1:   6]) = [  5.84444E-01 0.00176  4.31506E-01 0.00188  7.62279E-01 0.00171 ];
INELAXS                   (idx, [1:   6]) = [  7.99364E-03 0.00720  1.48401E-02 0.00594  3.26254E-17 0.00305 ];
SCATTXS                   (idx, [1:   6]) = [  5.92438E-01 0.00168  4.46346E-01 0.00168  7.62279E-01 0.00171 ];
SCATTPRODXS               (idx, [1:   6]) = [  5.92496E-01 0.00168  4.46456E-01 0.00168  7.62279E-01 0.00171 ];
REMXS                     (idx, [1:   6]) = [  1.92726E-02 0.00642  2.57646E-02 0.00757  3.45919E-02 0.00687 ];
NUBAR                     (idx, [1:   6]) = [  4.19288E-01 0.07035  4.19288E-01 0.07035  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  7.33382E-05 0.07571  1.36639E-04 0.07529  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  7.62193E-07 0.00584  7.57215E-09 0.00602  1.63319E-06 0.00361 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.56518E-01 0.00037  0.00000E+00 0.0E+00  4.34821E-02 0.00817  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  4.26903E-01 0.00166  0.00000E+00 0.0E+00  1.94839E-02 0.00881  7.61723E-01 0.00178 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.56732E-01 0.00037  0.00000E+00 0.0E+00  4.34821E-02 0.00817  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  4.26997E-01 0.00165  0.00000E+00 0.0E+00  1.94839E-02 0.00881  7.61723E-01 0.00178 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  5.92320E-01 0.00174  4.46387E-01 0.00172  7.61723E-01 0.00178 ];
SCATT1                    (idx, [1:   6]) = [  1.65320E-01 0.00280  1.46209E-01 0.00367  1.88160E-01 0.00414 ];
SCATT2                    (idx, [1:   6]) = [  5.77294E-02 0.00570  5.86737E-02 0.00688  5.66748E-02 0.00980 ];
SCATT3                    (idx, [1:   6]) = [  8.43785E-03 0.03449  6.14148E-03 0.05879  1.10222E-02 0.04275 ];
SCATT4                    (idx, [1:   6]) = [ -4.49997E-03 0.05565 -3.75015E-03 0.08541 -5.44336E-03 0.07534 ];
SCATT5                    (idx, [1:   6]) = [  1.09136E-03 0.20433  1.77012E-03 0.15440  3.74574E-04 0.97031 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  4.46322E-01 0.00215  3.06552E-01 0.00221  6.08154E-01 0.00208 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  7.50324E-01 0.00216  1.09276E+00 0.00225  5.50471E-01 0.00208 ];
P1_MUBAR                  (idx, [1:   6]) = [  2.79377E-01 0.00260  3.27456E-01 0.00317  2.47049E-01 0.00378 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.90316E-02 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -2.52414E-02 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  3.27926E-01 0.0E+00  2.43758E-01 0.0E+00  5.46261E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.01649E+00 0.0E+00  1.36748E+00 0.0E+00  6.10209E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98270 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '311' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  3.28171E+15 0.00297  1.65281E+15 0.00372  1.62891E+15 0.00373 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  6.32294E-01 0.00104  4.67111E-01 0.00103  7.99981E-01 0.00101 ];
FISSXS                    (idx, [1:   6]) = [  1.20702E-04 0.00826  2.39528E-04 0.00790  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  2.04152E-02 0.00269  6.57464E-03 0.00448  3.44550E-02 0.00238 ];
ABSXS                     (idx, [1:   6]) = [  2.05359E-02 0.00266  6.81417E-03 0.00429  3.44550E-02 0.00238 ];
RABSXS                    (idx, [1:   6]) = [  2.04947E-02 0.00267  6.73266E-03 0.00436  3.44550E-02 0.00238 ];
ELAXS                     (idx, [1:   6]) = [  6.05055E-01 0.00106  4.47001E-01 0.00113  7.65526E-01 0.00101 ];
INELAXS                   (idx, [1:   6]) = [  6.70287E-03 0.00483  1.32960E-02 0.00405  3.29388E-17 0.00186 ];
SCATTXS                   (idx, [1:   6]) = [  6.11758E-01 0.00102  4.60297E-01 0.00102  7.65526E-01 0.00101 ];
SCATTPRODXS               (idx, [1:   6]) = [  6.11799E-01 0.00102  4.60378E-01 0.00102  7.65526E-01 0.00101 ];
REMXS                     (idx, [1:   6]) = [  2.06546E-02 0.00375  2.81056E-02 0.00463  3.48444E-02 0.00392 ];
NUBAR                     (idx, [1:   6]) = [  7.57569E-01 0.04730  7.57569E-01 0.04730  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  9.37960E-05 0.04947  1.85584E-04 0.04925  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  8.30794E-07 0.00335  8.19657E-09 0.00346  1.66373E-06 0.00207 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.53665E-01 0.00024  0.00000E+00 0.0E+00  4.63352E-02 0.00495  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  4.38912E-01 0.00099  0.00000E+00 0.0E+00  2.13578E-02 0.00532  7.65137E-01 0.00106 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.53867E-01 0.00024  0.00000E+00 0.0E+00  4.63352E-02 0.00495  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  4.39006E-01 0.00099  0.00000E+00 0.0E+00  2.13578E-02 0.00532  7.65137E-01 0.00106 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  6.11592E-01 0.00105  4.60270E-01 0.00103  7.65137E-01 0.00106 ];
SCATT1                    (idx, [1:   6]) = [  1.67929E-01 0.00180  1.49477E-01 0.00239  1.86728E-01 0.00240 ];
SCATT2                    (idx, [1:   6]) = [  5.72519E-02 0.00364  5.91261E-02 0.00427  5.53911E-02 0.00602 ];
SCATT3                    (idx, [1:   6]) = [  8.32742E-03 0.02067  5.21619E-03 0.04214  1.14795E-02 0.02347 ];
SCATT4                    (idx, [1:   6]) = [ -4.92040E-03 0.03238 -4.19377E-03 0.04777 -5.65834E-03 0.04342 ];
SCATT5                    (idx, [1:   6]) = [  8.16640E-04 0.16699  1.34800E-03 0.13082  3.07261E-04 0.68196 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  4.64365E-01 0.00125  3.17634E-01 0.00131  6.13254E-01 0.00121 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  7.18951E-01 0.00125  1.05123E+00 0.00132  5.44344E-01 0.00121 ];
P1_MUBAR                  (idx, [1:   6]) = [  2.74633E-01 0.00160  3.24674E-01 0.00204  2.44050E-01 0.00216 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.35281E-02 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -2.82215E-02 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  3.49108E-01 0.0E+00  2.56780E-01 0.0E+00  5.49456E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  9.54815E-01 0.0E+00  1.29813E+00 0.0E+00  6.06661E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98270 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '312' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  6.94239E+15 0.00204  3.40249E+15 0.00252  3.53991E+15 0.00257 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  6.39068E-01 0.00068  4.70821E-01 0.00074  8.00914E-01 0.00065 ];
FISSXS                    (idx, [1:   6]) = [  1.09852E-04 0.00627  2.23982E-04 0.00595  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  2.08899E-02 0.00178  6.67220E-03 0.00321  3.45582E-02 0.00154 ];
ABSXS                     (idx, [1:   6]) = [  2.09997E-02 0.00176  6.89618E-03 0.00308  3.45582E-02 0.00154 ];
RABSXS                    (idx, [1:   6]) = [  2.09663E-02 0.00176  6.82811E-03 0.00311  3.45582E-02 0.00154 ];
ELAXS                     (idx, [1:   6]) = [  6.11753E-01 0.00069  4.51048E-01 0.00082  7.66356E-01 0.00065 ];
INELAXS                   (idx, [1:   6]) = [  6.31533E-03 0.00361  1.28762E-02 0.00304  3.29464E-17 0.00128 ];
SCATTXS                   (idx, [1:   6]) = [  6.18068E-01 0.00066  4.63924E-01 0.00074  7.66356E-01 0.00065 ];
SCATTPRODXS               (idx, [1:   6]) = [  6.18102E-01 0.00066  4.63993E-01 0.00074  7.66356E-01 0.00065 ];
REMXS                     (idx, [1:   6]) = [  2.10188E-02 0.00235  2.87498E-02 0.00295  3.47341E-02 0.00257 ];
NUBAR                     (idx, [1:   6]) = [  1.25272E+00 0.03082  1.25272E+00 0.03082  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  1.42308E-04 0.03230  2.88954E-04 0.03218  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  8.58086E-07 0.00223  8.42693E-09 0.00254  1.67419E-06 0.00137 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.52702E-01 0.00016  0.00000E+00 0.0E+00  4.72978E-02 0.00319  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  4.42007E-01 0.00073  0.00000E+00 0.0E+00  2.19585E-02 0.00347  7.66180E-01 0.00068 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.52841E-01 0.00016  0.00000E+00 0.0E+00  4.72978E-02 0.00319  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  4.42071E-01 0.00073  0.00000E+00 0.0E+00  2.19585E-02 0.00347  7.66180E-01 0.00068 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  6.18018E-01 0.00069  4.63965E-01 0.00076  7.66180E-01 0.00068 ];
SCATT1                    (idx, [1:   6]) = [  1.69471E-01 0.00123  1.51170E-01 0.00166  1.87149E-01 0.00169 ];
SCATT2                    (idx, [1:   6]) = [  5.74137E-02 0.00255  5.91584E-02 0.00311  5.57719E-02 0.00418 ];
SCATT3                    (idx, [1:   6]) = [  8.08899E-03 0.01511  4.77812E-03 0.03234  1.12526E-02 0.01679 ];
SCATT4                    (idx, [1:   6]) = [ -5.15288E-03 0.02065 -4.86578E-03 0.02878 -5.44421E-03 0.02976 ];
SCATT5                    (idx, [1:   6]) = [  9.26794E-04 0.10649  1.41070E-03 0.08462  4.58535E-04 0.32589 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  4.69596E-01 0.00085  3.19651E-01 0.00096  6.13765E-01 0.00081 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  7.10337E-01 0.00085  1.04377E+00 0.00097  5.43455E-01 0.00081 ];
P1_MUBAR                  (idx, [1:   6]) = [  2.74251E-01 0.00113  3.25794E-01 0.00142  2.44271E-01 0.00157 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.21221E-02 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -2.92303E-02 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  3.55470E-01 0.0E+00  2.59771E-01 0.0E+00  5.50215E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  9.37725E-01 0.0E+00  1.28318E+00 0.0E+00  6.05824E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98270 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '313' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  1.42593E+16 0.00143  6.88865E+15 0.00185  7.37065E+15 0.00168 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  6.42312E-01 0.00047  4.73443E-01 0.00051  8.00160E-01 0.00047 ];
FISSXS                    (idx, [1:   6]) = [  1.02851E-04 0.00426  2.12872E-04 0.00408  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  2.11303E-02 0.00120  6.74803E-03 0.00223  3.45692E-02 0.00108 ];
ABSXS                     (idx, [1:   6]) = [  2.12332E-02 0.00119  6.96090E-03 0.00216  3.45692E-02 0.00108 ];
RABSXS                    (idx, [1:   6]) = [  2.12031E-02 0.00119  6.89882E-03 0.00218  3.45692E-02 0.00108 ];
ELAXS                     (idx, [1:   6]) = [  6.14986E-01 0.00048  4.53873E-01 0.00056  7.65591E-01 0.00047 ];
INELAXS                   (idx, [1:   6]) = [  6.09248E-03 0.00245  1.26087E-02 0.00205  3.31302E-17 0.00088 ];
SCATTXS                   (idx, [1:   6]) = [  6.21079E-01 0.00046  4.66482E-01 0.00051  7.65591E-01 0.00047 ];
SCATTPRODXS               (idx, [1:   6]) = [  6.21109E-01 0.00046  4.66544E-01 0.00051  7.65591E-01 0.00047 ];
REMXS                     (idx, [1:   6]) = [  2.11915E-02 0.00165  2.91892E-02 0.00218  3.45591E-02 0.00174 ];
NUBAR                     (idx, [1:   6]) = [  1.86700E+00 0.01738  1.86700E+00 0.01738  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  1.92956E-04 0.01809  3.99360E-04 0.01806  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  8.70086E-07 0.00146  8.52152E-09 0.00171  1.67491E-06 0.00095 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.52241E-01 0.00011  0.00000E+00 0.0E+00  4.77591E-02 0.00229  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  4.44193E-01 0.00050  0.00000E+00 0.0E+00  2.22863E-02 0.00249  7.65601E-01 0.00049 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.52370E-01 0.00011  0.00000E+00 0.0E+00  4.77591E-02 0.00229  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  4.44254E-01 0.00050  0.00000E+00 0.0E+00  2.22863E-02 0.00249  7.65601E-01 0.00049 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  6.21092E-01 0.00048  4.66480E-01 0.00052  7.65601E-01 0.00049 ];
SCATT1                    (idx, [1:   6]) = [  1.69606E-01 0.00081  1.51449E-01 0.00120  1.86605E-01 0.00113 ];
SCATT2                    (idx, [1:   6]) = [  5.73241E-02 0.00180  5.92759E-02 0.00220  5.55064E-02 0.00284 ];
SCATT3                    (idx, [1:   6]) = [  8.06334E-03 0.01038  4.82316E-03 0.02298  1.10827E-02 0.01134 ];
SCATT4                    (idx, [1:   6]) = [ -5.27245E-03 0.01424 -4.75152E-03 0.02058 -5.76410E-03 0.01976 ];
SCATT5                    (idx, [1:   6]) = [  6.88363E-04 0.09847  1.42844E-03 0.06354  5.16171E-06 19.44605 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  4.72706E-01 0.00058  3.21994E-01 0.00065  6.13555E-01 0.00058 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  7.05401E-01 0.00059  1.03566E+00 0.00065  5.43462E-01 0.00058 ];
P1_MUBAR                  (idx, [1:   6]) = [  2.73097E-01 0.00075  3.24640E-01 0.00102  2.43744E-01 0.00105 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.19141E-02 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -2.97576E-02 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  3.61039E-01 0.0E+00  2.63892E-01 0.0E+00  5.50288E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  9.23261E-01 0.0E+00  1.26314E+00 0.0E+00  6.05744E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98270 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '314' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  2.93185E+16 0.00102  1.41200E+16 0.00136  1.51985E+16 0.00119 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  6.44099E-01 0.00032  4.76798E-01 0.00035  7.99529E-01 0.00033 ];
FISSXS                    (idx, [1:   6]) = [  9.71306E-05 0.00300  2.01703E-04 0.00291  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  2.11410E-02 0.00083  6.84518E-03 0.00157  3.44217E-02 0.00076 ];
ABSXS                     (idx, [1:   6]) = [  2.12381E-02 0.00082  7.04688E-03 0.00151  3.44217E-02 0.00076 ];
RABSXS                    (idx, [1:   6]) = [  2.12122E-02 0.00082  6.99314E-03 0.00153  3.44217E-02 0.00076 ];
ELAXS                     (idx, [1:   6]) = [  6.16952E-01 0.00033  4.57482E-01 0.00038  7.65107E-01 0.00033 ];
INELAXS                   (idx, [1:   6]) = [  5.90876E-03 0.00171  1.22690E-02 0.00147  3.47897E-17 0.00058 ];
SCATTXS                   (idx, [1:   6]) = [  6.22861E-01 0.00032  4.69751E-01 0.00035  7.65107E-01 0.00033 ];
SCATTPRODXS               (idx, [1:   6]) = [  6.22887E-01 0.00032  4.69804E-01 0.00034  7.65107E-01 0.00033 ];
REMXS                     (idx, [1:   6]) = [  2.12495E-02 0.00120  2.97453E-02 0.00148  3.44674E-02 0.00128 ];
NUBAR                     (idx, [1:   6]) = [  2.25192E+00 0.00872  2.25192E+00 0.00872  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  2.19178E-04 0.00929  4.54978E-04 0.00926  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  8.67602E-07 0.00105  8.66360E-09 0.00121  1.66534E-06 0.00066 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.51650E-01 7.8E-05  0.00000E+00 0.0E+00  4.83496E-02 0.00153  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  4.47001E-01 0.00034  0.00000E+00 0.0E+00  2.27142E-02 0.00168  7.65062E-01 0.00034 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.51761E-01 7.8E-05  0.00000E+00 0.0E+00  4.83496E-02 0.00153  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  4.47052E-01 0.00034  0.00000E+00 0.0E+00  2.27142E-02 0.00168  7.65062E-01 0.00034 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  6.22824E-01 0.00033  4.69715E-01 0.00035  7.65062E-01 0.00034 ];
SCATT1                    (idx, [1:   6]) = [  1.70082E-01 0.00058  1.52105E-01 0.00086  1.86798E-01 0.00080 ];
SCATT2                    (idx, [1:   6]) = [  5.75695E-02 0.00130  5.96617E-02 0.00155  5.56281E-02 0.00205 ];
SCATT3                    (idx, [1:   6]) = [  8.15996E-03 0.00749  4.68065E-03 0.01661  1.13890E-02 0.00807 ];
SCATT4                    (idx, [1:   6]) = [ -5.25494E-03 0.01013 -4.97010E-03 0.01348 -5.52259E-03 0.01435 ];
SCATT5                    (idx, [1:   6]) = [  8.58359E-04 0.05310  1.28135E-03 0.04525  4.64040E-04 0.15114 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  4.74017E-01 0.00040  3.24692E-01 0.00044  6.12731E-01 0.00041 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  7.03321E-01 0.00040  1.02681E+00 0.00044  5.44106E-01 0.00041 ];
P1_MUBAR                  (idx, [1:   6]) = [  2.73089E-01 0.00053  3.23809E-01 0.00072  2.44167E-01 0.00076 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.10218E-02 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -2.98714E-02 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  3.64462E-01 0.0E+00  2.67504E-01 0.0E+00  5.49390E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  9.14589E-01 0.0E+00  1.24609E+00 0.0E+00  6.06734E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98270 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '315' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  6.02074E+16 0.00073  2.92933E+16 0.00089  3.09141E+16 0.00090 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  6.41808E-01 0.00023  4.79729E-01 0.00024  7.95404E-01 0.00023 ];
FISSXS                    (idx, [1:   6]) = [  9.23972E-05 0.00220  1.89899E-04 0.00211  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  2.07971E-02 0.00061  6.91971E-03 0.00109  3.39475E-02 0.00054 ];
ABSXS                     (idx, [1:   6]) = [  2.08895E-02 0.00060  7.10961E-03 0.00105  3.39475E-02 0.00054 ];
RABSXS                    (idx, [1:   6]) = [  2.08658E-02 0.00060  7.06083E-03 0.00106  3.39475E-02 0.00054 ];
ELAXS                     (idx, [1:   6]) = [  6.15118E-01 0.00023  4.60698E-01 0.00026  7.61457E-01 0.00023 ];
INELAXS                   (idx, [1:   6]) = [  5.80040E-03 0.00122  1.19208E-02 0.00103  3.31731E-17 0.00040 ];
SCATTXS                   (idx, [1:   6]) = [  6.20918E-01 0.00022  4.72619E-01 0.00024  7.61457E-01 0.00023 ];
SCATTPRODXS               (idx, [1:   6]) = [  6.20942E-01 0.00022  4.72668E-01 0.00024  7.61457E-01 0.00023 ];
REMXS                     (idx, [1:   6]) = [  2.08868E-02 0.00084  3.01651E-02 0.00102  3.39661E-02 0.00089 ];
NUBAR                     (idx, [1:   6]) = [  2.39152E+00 0.00306  2.39152E+00 0.00306  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  2.21015E-04 0.00385  4.54277E-04 0.00381  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  8.44334E-07 0.00076  8.79048E-09 0.00087  1.63602E-06 0.00049 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.51174E-01 5.5E-05  0.00000E+00 0.0E+00  4.88264E-02 0.00108  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  4.49515E-01 0.00023  0.00000E+00 0.0E+00  2.30766E-02 0.00117  7.61438E-01 0.00024 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.51276E-01 5.5E-05  0.00000E+00 0.0E+00  4.88264E-02 0.00108  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  4.49563E-01 0.00023  0.00000E+00 0.0E+00  2.30766E-02 0.00117  7.61438E-01 0.00024 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  6.20897E-01 0.00023  4.72592E-01 0.00024  7.61438E-01 0.00024 ];
SCATT1                    (idx, [1:   6]) = [  1.70564E-01 0.00042  1.53079E-01 0.00058  1.87140E-01 0.00056 ];
SCATT2                    (idx, [1:   6]) = [  5.78256E-02 0.00082  5.96799E-02 0.00106  5.60702E-02 0.00136 ];
SCATT3                    (idx, [1:   6]) = [  7.86925E-03 0.00501  4.35991E-03 0.01159  1.11925E-02 0.00542 ];
SCATT4                    (idx, [1:   6]) = [ -5.48208E-03 0.00664 -5.27500E-03 0.00886 -5.67937E-03 0.00962 ];
SCATT5                    (idx, [1:   6]) = [  7.43140E-04 0.04503  1.19286E-03 0.03537  3.16981E-04 0.15816 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  4.71244E-01 0.00028  3.26650E-01 0.00031  6.08264E-01 0.00029 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  7.07404E-01 0.00028  1.02056E+00 0.00031  5.48053E-01 0.00029 ];
P1_MUBAR                  (idx, [1:   6]) = [  2.74708E-01 0.00038  3.23908E-01 0.00049  2.45774E-01 0.00052 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.05183E-02 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -2.92272E-02 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  3.64986E-01 0.0E+00  2.70508E-01 0.0E+00  5.45436E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  9.13278E-01 0.0E+00  1.23225E+00 0.0E+00  6.11132E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98270 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '316' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  1.22138E+17 0.00054  6.13855E+16 0.00063  6.07520E+16 0.00065 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  6.35043E-01 0.00016  4.82185E-01 0.00016  7.89500E-01 0.00017 ];
FISSXS                    (idx, [1:   6]) = [  8.98642E-05 0.00151  1.78796E-04 0.00146  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  2.00248E-02 0.00042  6.95545E-03 0.00072  3.32307E-02 0.00039 ];
ABSXS                     (idx, [1:   6]) = [  2.01146E-02 0.00042  7.13425E-03 0.00070  3.32307E-02 0.00039 ];
RABSXS                    (idx, [1:   6]) = [  2.00939E-02 0.00042  7.09301E-03 0.00071  3.32307E-02 0.00039 ];
ELAXS                     (idx, [1:   6]) = [  6.09076E-01 0.00016  4.63407E-01 0.00017  7.56269E-01 0.00017 ];
INELAXS                   (idx, [1:   6]) = [  5.85221E-03 0.00081  1.16436E-02 0.00069  3.39493E-17 0.00032 ];
SCATTXS                   (idx, [1:   6]) = [  6.14928E-01 0.00015  4.75051E-01 0.00015  7.56269E-01 0.00017 ];
SCATTPRODXS               (idx, [1:   6]) = [  6.14949E-01 0.00015  4.75092E-01 0.00015  7.56269E-01 0.00017 ];
REMXS                     (idx, [1:   6]) = [  2.00973E-02 0.00061  3.03138E-02 0.00070  3.32468E-02 0.00064 ];
NUBAR                     (idx, [1:   6]) = [  2.38729E+00 0.00105  2.38729E+00 0.00105  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  2.14541E-04 0.00186  4.26853E-04 0.00182  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  7.94449E-07 0.00054  8.85020E-09 0.00056  1.58821E-06 0.00035 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.51107E-01 3.7E-05  0.00000E+00 0.0E+00  4.88933E-02 0.00072  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  4.51830E-01 0.00015  0.00000E+00 0.0E+00  2.32277E-02 0.00077  7.56253E-01 0.00018 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.51194E-01 3.7E-05  0.00000E+00 0.0E+00  4.88933E-02 0.00072  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  4.51871E-01 0.00015  0.00000E+00 0.0E+00  2.32277E-02 0.00077  7.56253E-01 0.00018 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  6.14924E-01 0.00016  4.75058E-01 0.00016  7.56253E-01 0.00018 ];
SCATT1                    (idx, [1:   6]) = [  1.70813E-01 0.00029  1.53827E-01 0.00039  1.87981E-01 0.00041 ];
SCATT2                    (idx, [1:   6]) = [  5.83968E-02 0.00059  5.98303E-02 0.00072  5.69485E-02 0.00095 ];
SCATT3                    (idx, [1:   6]) = [  7.68105E-03 0.00377  4.23731E-03 0.00857  1.11595E-02 0.00384 ];
SCATT4                    (idx, [1:   6]) = [ -5.58330E-03 0.00446 -5.43704E-03 0.00582 -5.73190E-03 0.00649 ];
SCATT5                    (idx, [1:   6]) = [  5.81024E-04 0.03970  1.12507E-03 0.02613  3.22422E-05 1.08116 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  4.64230E-01 0.00019  3.28358E-01 0.00021  6.01519E-01 0.00020 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  7.18062E-01 0.00019  1.01520E+00 0.00021  5.54175E-01 0.00020 ];
P1_MUBAR                  (idx, [1:   6]) = [  2.77780E-01 0.00026  3.23805E-01 0.00034  2.48568E-01 0.00037 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.04631E-02 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -2.77251E-02 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  3.62345E-01 0.0E+00  2.73393E-01 0.0E+00  5.39741E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  9.19932E-01 0.0E+00  1.21925E+00 0.0E+00  6.17581E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98270 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '317' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  2.41006E+17 0.00041  1.30000E+17 0.00047  1.11007E+17 0.00051 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  6.19493E-01 0.00011  4.83080E-01 0.00011  7.79249E-01 0.00012 ];
FISSXS                    (idx, [1:   6]) = [  9.23464E-05 0.00107  1.71200E-04 0.00104  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  1.85038E-02 0.00032  6.94360E-03 0.00051  3.20420E-02 0.00030 ];
ABSXS                     (idx, [1:   6]) = [  1.85961E-02 0.00032  7.11480E-03 0.00050  3.20420E-02 0.00030 ];
RABSXS                    (idx, [1:   6]) = [  1.85760E-02 0.00032  7.07754E-03 0.00050  3.20420E-02 0.00030 ];
ELAXS                     (idx, [1:   6]) = [  5.94703E-01 0.00012  4.64483E-01 0.00012  7.47207E-01 0.00012 ];
INELAXS                   (idx, [1:   6]) = [  6.19404E-03 0.00056  1.14830E-02 0.00049  3.48967E-17 0.00023 ];
SCATTXS                   (idx, [1:   6]) = [  6.00897E-01 0.00011  4.75966E-01 0.00011  7.47207E-01 0.00012 ];
SCATTPRODXS               (idx, [1:   6]) = [  6.00917E-01 0.00011  4.76003E-01 0.00011  7.47207E-01 0.00012 ];
REMXS                     (idx, [1:   6]) = [  1.85736E-02 0.00044  2.99513E-02 0.00048  3.20406E-02 0.00048 ];
NUBAR                     (idx, [1:   6]) = [  2.38251E+00 0.00078  2.38251E+00 0.00078  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  2.20027E-04 0.00136  4.07907E-04 0.00134  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  6.98289E-07 0.00043  8.78592E-09 0.00039  1.50574E-06 0.00027 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.51939E-01 2.6E-05  0.00000E+00 0.0E+00  4.80613E-02 0.00052  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  4.53091E-01 0.00011  0.00000E+00 0.0E+00  2.28759E-02 0.00056  7.47208E-01 0.00013 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.52019E-01 2.6E-05  0.00000E+00 0.0E+00  4.80613E-02 0.00052  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  4.53129E-01 0.00011  0.00000E+00 0.0E+00  2.28759E-02 0.00056  7.47208E-01 0.00013 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  6.00899E-01 0.00011  4.75967E-01 0.00011  7.47208E-01 0.00013 ];
SCATT1                    (idx, [1:   6]) = [  1.70384E-01 0.00021  1.54028E-01 0.00027  1.89542E-01 0.00029 ];
SCATT2                    (idx, [1:   6]) = [  5.91943E-02 0.00041  5.98254E-02 0.00050  5.84558E-02 0.00065 ];
SCATT3                    (idx, [1:   6]) = [  7.28078E-03 0.00276  4.08913E-03 0.00617  1.10185E-02 0.00292 ];
SCATT4                    (idx, [1:   6]) = [ -5.77753E-03 0.00313 -5.57331E-03 0.00415 -6.01678E-03 0.00486 ];
SCATT5                    (idx, [1:   6]) = [  5.11734E-04 0.03094  1.05376E-03 0.01927 -1.22626E-04 0.21239 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  4.49109E-01 0.00014  3.29053E-01 0.00014  5.89707E-01 0.00015 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  7.42224E-01 0.00014  1.01303E+00 0.00014  5.65265E-01 0.00015 ];
P1_MUBAR                  (idx, [1:   6]) = [  2.83549E-01 0.00019  3.23608E-01 0.00023  2.53667E-01 0.00027 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.17644E-02 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -2.47643E-02 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  3.53376E-01 0.0E+00  2.75097E-01 0.0E+00  5.29923E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  9.43281E-01 0.0E+00  1.21169E+00 0.0E+00  6.29022E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98269 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '318' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  4.50951E+17 0.00032  2.74966E+17 0.00034  1.75985E+17 0.00041 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  5.90477E-01 7.9E-05  4.80650E-01 7.5E-05  7.62078E-01 9.7E-05 ];
FISSXS                    (idx, [1:   6]) = [  1.03789E-04 0.00075  1.70216E-04 0.00073  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  1.58691E-02 0.00025  6.76045E-03 0.00034  3.01010E-02 0.00025 ];
ABSXS                     (idx, [1:   6]) = [  1.59729E-02 0.00025  6.93066E-03 0.00033  3.01010E-02 0.00025 ];
RABSXS                    (idx, [1:   6]) = [  1.59514E-02 0.00025  6.89536E-03 0.00033  3.01010E-02 0.00025 ];
ELAXS                     (idx, [1:   6]) = [  5.67405E-01 8.1E-05  4.62077E-01 8.2E-05  7.31976E-01 9.7E-05 ];
INELAXS                   (idx, [1:   6]) = [  7.09926E-03 0.00038  1.16429E-02 0.00034  3.01687E-17 0.00018 ];
SCATTXS                   (idx, [1:   6]) = [  5.74504E-01 7.7E-05  4.73720E-01 7.5E-05  7.31976E-01 9.7E-05 ];
SCATTPRODXS               (idx, [1:   6]) = [  5.74525E-01 7.7E-05  4.73755E-01 7.5E-05  7.31976E-01 9.7E-05 ];
REMXS                     (idx, [1:   6]) = [  1.59519E-02 0.00035  2.84965E-02 0.00033  3.00895E-02 0.00040 ];
NUBAR                     (idx, [1:   6]) = [  2.37750E+00 0.00048  2.37750E+00 0.00048  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  2.46759E-04 0.00090  4.04691E-04 0.00089  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  5.37730E-07 0.00036  8.43815E-09 0.00027  1.36471E-06 0.00023 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.54419E-01 1.7E-05  0.00000E+00 0.0E+00  4.55810E-02 0.00035  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  4.52119E-01 7.4E-05  0.00000E+00 0.0E+00  2.15923E-02 0.00038  7.31988E-01 0.00010 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.54494E-01 1.7E-05  0.00000E+00 0.0E+00  4.55810E-02 0.00035  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  4.52154E-01 7.4E-05  0.00000E+00 0.0E+00  2.15923E-02 0.00038  7.31988E-01 0.00010 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  5.74503E-01 8.1E-05  4.73711E-01 7.6E-05  7.31988E-01 0.00010 ];
SCATT1                    (idx, [1:   6]) = [  1.68453E-01 0.00015  1.53252E-01 0.00018  1.92206E-01 0.00022 ];
SCATT2                    (idx, [1:   6]) = [  6.00962E-02 0.00029  5.95902E-02 0.00035  6.08876E-02 0.00053 ];
SCATT3                    (idx, [1:   6]) = [  6.66978E-03 0.00223  4.12788E-03 0.00420  1.06410E-02 0.00254 ];
SCATT4                    (idx, [1:   6]) = [ -5.85414E-03 0.00211 -5.48481E-03 0.00273 -6.43168E-03 0.00356 ];
SCATT5                    (idx, [1:   6]) = [  4.46806E-04 0.02664  1.03222E-03 0.01330 -4.68203E-04 0.04481 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  4.22024E-01 1.0E-04  3.27399E-01 1.0E-04  5.69871E-01 0.00012 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  7.89853E-01 1.0E-04  1.01814E+00 1.0E-04  5.84936E-01 0.00012 ];
P1_MUBAR                  (idx, [1:   6]) = [  2.93216E-01 0.00013  3.23513E-01 0.00016  2.62582E-01 0.00020 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.53269E-02 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -1.99161E-02 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  3.35356E-01 0.0E+00  2.74325E-01 0.0E+00  5.13979E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  9.93967E-01 0.0E+00  1.21511E+00 0.0E+00  6.48535E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98269 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '319' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  7.73017E+17 0.00026  5.68655E+17 0.00027  2.04362E+17 0.00037 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  5.11665E-01 5.8E-05  4.48536E-01 5.4E-05  6.87328E-01 8.4E-05 ];
FISSXS                    (idx, [1:   6]) = [  1.39220E-04 0.00048  1.89252E-04 0.00047  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  1.15198E-02 0.00022  6.15185E-03 0.00024  2.64569E-02 0.00027 ];
ABSXS                     (idx, [1:   6]) = [  1.16591E-02 0.00022  6.34111E-03 0.00023  2.64569E-02 0.00027 ];
RABSXS                    (idx, [1:   6]) = [  1.16310E-02 0.00022  6.30297E-03 0.00024  2.64569E-02 0.00027 ];
ELAXS                     (idx, [1:   6]) = [  4.90664E-01 6.1E-05  4.29496E-01 5.9E-05  6.60871E-01 8.4E-05 ];
INELAXS                   (idx, [1:   6]) = [  9.34154E-03 0.00025  1.26986E-02 0.00022  2.51189E-17 0.00019 ];
SCATTXS                   (idx, [1:   6]) = [  5.00006E-01 5.7E-05  4.42195E-01 5.3E-05  6.60871E-01 8.4E-05 ];
SCATTPRODXS               (idx, [1:   6]) = [  5.00034E-01 5.7E-05  4.42233E-01 5.3E-05  6.60871E-01 8.4E-05 ];
REMXS                     (idx, [1:   6]) = [  1.16325E-02 0.00032  2.28915E-02 0.00026  2.64531E-02 0.00040 ];
NUBAR                     (idx, [1:   6]) = [  2.37308E+00 0.00033  2.37308E+00 0.00033  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  3.30384E-04 0.00061  4.49114E-04 0.00060  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  2.95852E-07 0.00039  7.47678E-09 0.00020  1.09827E-06 0.00026 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.62494E-01 1.1E-05  0.00000E+00 0.0E+00  3.75061E-02 0.00028  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  4.25606E-01 5.2E-05  0.00000E+00 0.0E+00  1.65850E-02 0.00030  6.60875E-01 8.7E-05 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.62580E-01 1.1E-05  0.00000E+00 0.0E+00  3.75061E-02 0.00028  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  4.25645E-01 5.2E-05  0.00000E+00 0.0E+00  1.65850E-02 0.00030  6.60875E-01 8.7E-05 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  5.00004E-01 5.8E-05  4.42191E-01 5.4E-05  6.60875E-01 8.7E-05 ];
SCATT1                    (idx, [1:   6]) = [  1.48593E-01 0.00012  1.37773E-01 0.00014  1.78702E-01 0.00021 ];
SCATT2                    (idx, [1:   6]) = [  5.55937E-02 0.00023  5.42742E-02 0.00025  5.92657E-02 0.00046 ];
SCATT3                    (idx, [1:   6]) = [  5.71716E-03 0.00178  4.58822E-03 0.00248  8.85793E-03 0.00256 ];
SCATT4                    (idx, [1:   6]) = [ -4.82554E-03 0.00195 -4.13306E-03 0.00251 -6.75306E-03 0.00298 ];
SCATT5                    (idx, [1:   6]) = [  5.97477E-04 0.01400  1.18410E-03 0.00780 -1.03516E-03 0.01763 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  3.63072E-01 7.2E-05  3.10763E-01 7.3E-05  5.08626E-01 0.00011 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  9.18096E-01 7.2E-05  1.07263E+00 7.3E-05  6.55368E-01 0.00011 ];
P1_MUBAR                  (idx, [1:   6]) = [  2.97183E-01 0.00010  3.11567E-01 0.00012  2.70403E-01 0.00019 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  2.82527E-02 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -1.23424E-02 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.94348E-01 0.0E+00  2.59738E-01 0.0E+00  4.67734E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.13244E+00 0.0E+00  1.28335E+00 0.0E+00  7.12656E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98269 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '320' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  1.17175E+18 0.00022  1.03493E+18 0.00023  1.36818E+17 0.00033 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  4.07549E-01 3.9E-05  3.82844E-01 3.8E-05  5.94426E-01 7.6E-05 ];
FISSXS                    (idx, [1:   6]) = [  7.38076E-03 0.00025  1.92584E-03 0.00012  4.86435E-02 0.00022 ];
CAPTXS                    (idx, [1:   6]) = [  7.95224E-03 0.00019  5.40355E-03 0.00020  2.72318E-02 0.00032 ];
ABSXS                     (idx, [1:   6]) = [  1.53330E-02 0.00019  7.32938E-03 0.00016  7.58753E-02 0.00022 ];
RABSXS                    (idx, [1:   6]) = [  1.52922E-02 0.00019  7.28317E-03 0.00016  7.58753E-02 0.00022 ];
ELAXS                     (idx, [1:   6]) = [  3.79501E-01 4.1E-05  3.61119E-01 4.3E-05  5.18550E-01 7.1E-05 ];
INELAXS                   (idx, [1:   6]) = [  1.27141E-02 0.00016  1.43949E-02 0.00015  2.27768E-17 0.00022 ];
SCATTXS                   (idx, [1:   6]) = [  3.92216E-01 3.6E-05  3.75514E-01 3.7E-05  5.18550E-01 7.1E-05 ];
SCATTPRODXS               (idx, [1:   6]) = [  3.92256E-01 3.6E-05  3.75560E-01 3.7E-05  5.18550E-01 7.1E-05 ];
REMXS                     (idx, [1:   6]) = [  1.52917E-02 0.00023  1.64484E-02 0.00024  7.58655E-02 0.00028 ];
NUBAR                     (idx, [1:   6]) = [  2.49285E+00 9.2E-06  2.50970E+00 4.0E-05  2.48781E+00 4.3E-08 ];
NSF                       (idx, [1:   6]) = [  1.83991E-02 0.00025  4.83326E-03 0.00012  1.21016E-01 0.00022 ];
RECIPVEL                  (idx, [1:   6]) = [  7.29328E-08 0.00042  6.10891E-09 0.00017  5.78402E-07 0.00034 ];
FISSE                     (idx, [1:   6]) = [  1.99207E+02 1.4E-07  1.98984E+02 4.6E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 1.8E-07  6.89452E-07 0.26552 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 1.5E-07  4.44203E-07 0.33201 ];
CHID                      (idx, [1:   4]) = [  9.99918E-01 3.7E-05  8.18473E-05 0.44834 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.75595E-01 7.5E-06  0.00000E+00 0.0E+00  2.44046E-02 0.00030  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  3.66349E-01 3.8E-05  0.00000E+00 0.0E+00  9.16429E-03 0.00031  5.18560E-01 8.4E-05 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.75718E-01 7.5E-06  0.00000E+00 0.0E+00  2.44046E-02 0.00030  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  3.66395E-01 3.8E-05  0.00000E+00 0.0E+00  9.16429E-03 0.00031  5.18560E-01 8.4E-05 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  3.92216E-01 3.9E-05  3.75513E-01 3.9E-05  5.18560E-01 8.4E-05 ];
SCATT1                    (idx, [1:   6]) = [  1.08610E-01 0.00011  1.04540E-01 0.00011  1.39397E-01 0.00027 ];
SCATT2                    (idx, [1:   6]) = [  4.34510E-02 0.00020  4.26572E-02 0.00021  4.94552E-02 0.00061 ];
SCATT3                    (idx, [1:   6]) = [  5.41368E-03 0.00148  5.47168E-03 0.00151  4.97471E-03 0.00509 ];
SCATT4                    (idx, [1:   6]) = [ -1.90754E-03 0.00347 -1.29258E-03 0.00537 -6.55935E-03 0.00327 ];
SCATT5                    (idx, [1:   6]) = [  1.12643E-03 0.00529  1.47708E-03 0.00418 -1.52603E-03 0.01287 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.98938E-01 5.5E-05  2.78303E-01 5.7E-05  4.55028E-01 0.00011 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.11506E+00 5.5E-05  1.19774E+00 5.7E-05  7.32563E-01 0.00011 ];
P1_MUBAR                  (idx, [1:   6]) = [  2.76914E-01 1.0E-04  2.78393E-01 0.00011  2.68816E-01 0.00026 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.19983E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  2.74856E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  6.92348E-07 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.45891E-01 0.0E+00  2.32604E-01 0.0E+00  4.32872E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.35562E+00 0.0E+00  1.43305E+00 0.0E+00  7.70051E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98269 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '321' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  1.52042E+18 0.00020  1.43085E+18 0.00020  8.95682E+16 0.00038 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  3.41863E-01 3.4E-05  3.32126E-01 3.4E-05  4.97415E-01 7.7E-05 ];
FISSXS                    (idx, [1:   6]) = [  6.89478E-03 0.00021  3.38293E-03 0.00012  6.29973E-02 0.00025 ];
CAPTXS                    (idx, [1:   6]) = [  6.19609E-03 0.00017  4.88817E-03 0.00017  2.70909E-02 0.00042 ];
ABSXS                     (idx, [1:   6]) = [  1.30909E-02 0.00016  8.27110E-03 0.00014  9.00882E-02 0.00024 ];
RABSXS                    (idx, [1:   6]) = [  1.30502E-02 0.00016  8.22787E-03 0.00014  9.00882E-02 0.00024 ];
ELAXS                     (idx, [1:   6]) = [  3.15398E-01 3.7E-05  3.09644E-01 3.9E-05  4.07327E-01 5.8E-05 ];
INELAXS                   (idx, [1:   6]) = [  1.33744E-02 0.00014  1.42116E-02 0.00014  1.72889E-17 0.00029 ];
SCATTXS                   (idx, [1:   6]) = [  3.28772E-01 3.2E-05  3.23855E-01 3.3E-05  4.07327E-01 5.8E-05 ];
SCATTPRODXS               (idx, [1:   6]) = [  3.28813E-01 3.2E-05  3.23898E-01 3.3E-05  4.07327E-01 5.8E-05 ];
REMXS                     (idx, [1:   6]) = [  1.30488E-02 0.00024  1.29132E-02 0.00025  9.01095E-02 0.00032 ];
NUBAR                     (idx, [1:   6]) = [  2.50272E+00 1.1E-05  2.52000E+00 2.4E-05  2.48792E+00 6.7E-08 ];
NSF                       (idx, [1:   6]) = [  1.72557E-02 0.00021  8.52497E-03 0.00012  1.56732E-01 0.00025 ];
RECIPVEL                  (idx, [1:   6]) = [  2.21195E-08 0.00042  5.42723E-09 0.00018  2.88779E-07 0.00043 ];
FISSE                     (idx, [1:   6]) = [  1.99202E+02 1.3E-07  1.99119E+02 2.4E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 2.2E-07  1.17626E-06 0.18309 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 1.6E-07  6.52739E-07 0.24813 ];
CHID                      (idx, [1:   4]) = [  9.99837E-01 4.5E-05  1.63075E-04 0.27711 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.85525E-01 5.5E-06  0.00000E+00 0.0E+00  1.44754E-02 0.00037  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  3.19170E-01 3.5E-05  0.00000E+00 0.0E+00  4.68799E-03 0.00038  4.07305E-01 8.7E-05 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.85657E-01 5.6E-06  0.00000E+00 0.0E+00  1.44754E-02 0.00037  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  3.19213E-01 3.5E-05  0.00000E+00 0.0E+00  4.68799E-03 0.00038  4.07305E-01 8.7E-05 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  3.28774E-01 3.4E-05  3.23858E-01 3.6E-05  4.07305E-01 8.7E-05 ];
SCATT1                    (idx, [1:   6]) = [  7.65280E-02 0.00012  7.56901E-02 0.00012  8.99128E-02 0.00047 ];
SCATT2                    (idx, [1:   6]) = [  3.17019E-02 0.00022  3.16609E-02 0.00023  3.23562E-02 0.00098 ];
SCATT3                    (idx, [1:   6]) = [  5.19581E-03 0.00119  5.39203E-03 0.00118  2.06055E-03 0.01311 ];
SCATT4                    (idx, [1:   6]) = [  1.63447E-04 0.03332  4.80999E-04 0.01159 -4.90973E-03 0.00476 ];
SCATT5                    (idx, [1:   6]) = [  1.30581E-03 0.00369  1.45644E-03 0.00341 -1.10046E-03 0.01879 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.65335E-01 5.2E-05  2.56436E-01 5.4E-05  4.07502E-01 0.00014 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.25628E+00 5.2E-05  1.29987E+00 5.4E-05  8.18008E-01 0.00014 ];
P1_MUBAR                  (idx, [1:   6]) = [  2.32768E-01 0.00012  2.33714E-01 0.00012  2.20751E-01 0.00047 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.31815E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  3.31601E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  1.17900E-06 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.23355E-01 0.0E+00  2.17400E-01 0.0E+00  3.97067E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.49239E+00 0.0E+00  1.53327E+00 0.0E+00  8.39489E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98269 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '322' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  1.79366E+18 0.00018  1.71783E+18 0.00018  7.58355E+16 0.00042 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  3.23163E-01 3.2E-05  3.17380E-01 3.3E-05  4.54149E-01 8.2E-05 ];
FISSXS                    (idx, [1:   6]) = [  5.41680E-03 0.00019  3.27780E-03 9.5E-05  5.38700E-02 0.00028 ];
CAPTXS                    (idx, [1:   6]) = [  5.61137E-03 0.00016  4.72522E-03 0.00015  2.56857E-02 0.00048 ];
ABSXS                     (idx, [1:   6]) = [  1.10282E-02 0.00015  8.00302E-03 0.00012  7.95557E-02 0.00027 ];
RABSXS                    (idx, [1:   6]) = [  1.09905E-02 0.00015  7.96368E-03 0.00012  7.95557E-02 0.00027 ];
ELAXS                     (idx, [1:   6]) = [  2.98966E-01 3.6E-05  2.95628E-01 3.7E-05  3.74594E-01 6.0E-05 ];
INELAXS                   (idx, [1:   6]) = [  1.31679E-02 0.00013  1.37492E-02 0.00013  1.71705E-17 0.00033 ];
SCATTXS                   (idx, [1:   6]) = [  3.12134E-01 3.1E-05  3.09377E-01 3.2E-05  3.74594E-01 6.0E-05 ];
SCATTPRODXS               (idx, [1:   6]) = [  3.12172E-01 3.1E-05  3.09416E-01 3.2E-05  3.74594E-01 6.0E-05 ];
REMXS                     (idx, [1:   6]) = [  1.09915E-02 0.00025  1.13662E-02 0.00026  7.95241E-02 0.00038 ];
NUBAR                     (idx, [1:   6]) = [  2.50628E+00 1.3E-05  2.51954E+00 2.1E-05  2.48799E+00 8.9E-08 ];
NSF                       (idx, [1:   6]) = [  1.35760E-02 0.00019  8.25855E-03 9.6E-05  1.34028E-01 0.00028 ];
RECIPVEL                  (idx, [1:   6]) = [  1.39837E-08 0.00041  5.18372E-09 0.00015  2.13318E-07 0.00048 ];
FISSE                     (idx, [1:   6]) = [  1.99188E+02 1.5E-07  1.99126E+02 2.1E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 2.4E-07  1.26518E-06 0.18941 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 2.1E-07  9.61476E-07 0.22047 ];
CHID                      (idx, [1:   4]) = [  9.99908E-01 3.5E-05  9.20366E-05 0.37778 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.89010E-01 4.6E-06  0.00000E+00 0.0E+00  1.09896E-02 0.00042  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  3.05975E-01 3.4E-05  0.00000E+00 0.0E+00  3.39992E-03 0.00042  3.74625E-01 9.1E-05 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.89137E-01 4.7E-06  0.00000E+00 0.0E+00  1.09896E-02 0.00042  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  3.06014E-01 3.4E-05  0.00000E+00 0.0E+00  3.39992E-03 0.00042  3.74625E-01 9.1E-05 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  3.12134E-01 3.3E-05  3.09375E-01 3.4E-05  3.74625E-01 9.1E-05 ];
SCATT1                    (idx, [1:   6]) = [  6.67084E-02 0.00012  6.64564E-02 0.00012  7.24170E-02 0.00058 ];
SCATT2                    (idx, [1:   6]) = [  2.77505E-02 0.00023  2.78303E-02 0.00023  2.59427E-02 0.00123 ];
SCATT3                    (idx, [1:   6]) = [  4.90923E-03 0.00109  5.07119E-03 0.00107  1.24034E-03 0.02284 ];
SCATT4                    (idx, [1:   6]) = [  6.17090E-04 0.00807  8.25424E-04 0.00609 -4.10219E-03 0.00575 ];
SCATT5                    (idx, [1:   6]) = [  1.26036E-03 0.00348  1.35324E-03 0.00329 -8.43634E-04 0.02639 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.56454E-01 5.2E-05  2.50924E-01 5.3E-05  3.81732E-01 0.00015 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.29978E+00 5.2E-05  1.32843E+00 5.3E-05  8.73233E-01 0.00015 ];
P1_MUBAR                  (idx, [1:   6]) = [  2.13718E-01 0.00012  2.14809E-01 0.00013  1.93307E-01 0.00059 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.23105E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  1.96071E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  1.27116E-06 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.18820E-01 0.0E+00  2.14861E-01 0.0E+00  3.75507E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.52332E+00 0.0E+00  1.55139E+00 0.0E+00  8.87688E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98269 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '323' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  2.01013E+18 0.00017  1.94062E+18 0.00017  6.95126E+16 0.00044 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  3.12799E-01 3.0E-05  3.08571E-01 3.1E-05  4.30830E-01 9.5E-05 ];
FISSXS                    (idx, [1:   6]) = [  4.84476E-03 0.00017  3.21247E-03 9.7E-05  5.04152E-02 0.00029 ];
CAPTXS                    (idx, [1:   6]) = [  5.34048E-03 0.00015  4.63406E-03 0.00014  2.50633E-02 0.00053 ];
ABSXS                     (idx, [1:   6]) = [  1.01852E-02 0.00014  7.84654E-03 0.00011  7.54785E-02 0.00029 ];
RABSXS                    (idx, [1:   6]) = [  1.01499E-02 0.00014  7.80993E-03 0.00011  7.54785E-02 0.00029 ];
ELAXS                     (idx, [1:   6]) = [  2.89704E-01 3.3E-05  2.87353E-01 3.4E-05  3.55352E-01 6.9E-05 ];
INELAXS                   (idx, [1:   6]) = [  1.29098E-02 0.00012  1.33722E-02 0.00012  1.71337E-17 0.00035 ];
SCATTXS                   (idx, [1:   6]) = [  3.02614E-01 2.9E-05  3.00725E-01 3.0E-05  3.55352E-01 6.9E-05 ];
SCATTPRODXS               (idx, [1:   6]) = [  3.02649E-01 2.9E-05  3.00761E-01 3.0E-05  3.55352E-01 6.9E-05 ];
REMXS                     (idx, [1:   6]) = [  1.01489E-02 0.00026  1.04906E-02 0.00026  7.54667E-02 0.00041 ];
NUBAR                     (idx, [1:   6]) = [  2.50776E+00 1.3E-05  2.51885E+00 2.0E-05  2.48803E+00 9.5E-08 ];
NSF                       (idx, [1:   6]) = [  1.21495E-02 0.00017  8.09175E-03 9.7E-05  1.25434E-01 0.00029 ];
RECIPVEL                  (idx, [1:   6]) = [  1.14054E-08 0.00038  5.03827E-09 0.00015  1.89156E-07 0.00049 ];
FISSE                     (idx, [1:   6]) = [  1.99183E+02 1.5E-07  1.99132E+02 1.9E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 2.3E-07  1.21770E-06 0.18642 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 2.0E-07  9.14870E-07 0.21603 ];
CHID                      (idx, [1:   4]) = [  9.99914E-01 3.3E-05  8.60871E-05 0.37804 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.91084E-01 3.9E-06  0.00000E+00 0.0E+00  8.91564E-03 0.00043  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.98044E-01 3.3E-05  0.00000E+00 0.0E+00  2.68116E-03 0.00043  3.55364E-01 0.00010 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.91206E-01 3.9E-06  0.00000E+00 0.0E+00  8.91564E-03 0.00043  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.98081E-01 3.2E-05  0.00000E+00 0.0E+00  2.68116E-03 0.00043  3.55364E-01 0.00010 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  3.02615E-01 3.2E-05  3.00725E-01 3.2E-05  3.55364E-01 0.00010 ];
SCATT1                    (idx, [1:   6]) = [  6.06377E-02 0.00012  6.06170E-02 0.00012  6.12132E-02 0.00068 ];
SCATT2                    (idx, [1:   6]) = [  2.52362E-02 0.00023  2.53620E-02 0.00023  2.17220E-02 0.00152 ];
SCATT3                    (idx, [1:   6]) = [  4.68946E-03 0.00107  4.82548E-03 0.00106  8.91461E-04 0.03213 ];
SCATT4                    (idx, [1:   6]) = [  8.48554E-04 0.00533  1.00486E-03 0.00458 -3.51495E-03 0.00724 ];
SCATT5                    (idx, [1:   6]) = [  1.19862E-03 0.00335  1.26566E-03 0.00320 -6.73215E-04 0.03507 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.52161E-01 4.8E-05  2.47954E-01 4.8E-05  3.69617E-01 0.00017 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.32191E+00 4.8E-05  1.34434E+00 4.8E-05  9.01859E-01 0.00017 ];
P1_MUBAR                  (idx, [1:   6]) = [  2.00379E-01 0.00012  2.01570E-01 0.00012  1.72257E-01 0.00069 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.19254E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  1.48369E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  1.22296E-06 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.16906E-01 0.0E+00  2.13803E-01 0.0E+00  3.64629E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.53676E+00 0.0E+00  1.55907E+00 0.0E+00  9.14170E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98269 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '324' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  2.17488E+18 0.00015  2.11044E+18 0.00015  6.44482E+16 0.00047 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  3.05717E-01 3.0E-05  3.02372E-01 3.1E-05  4.15246E-01 0.00011 ];
FISSXS                    (idx, [1:   6]) = [  4.50184E-03 0.00017  3.16235E-03 9.5E-05  4.83662E-02 0.00032 ];
CAPTXS                    (idx, [1:   6]) = [  5.16102E-03 0.00015  4.56548E-03 0.00014  2.46640E-02 0.00053 ];
ABSXS                     (idx, [1:   6]) = [  9.66286E-03 0.00013  7.72784E-03 0.00011  7.30302E-02 0.00030 ];
RABSXS                    (idx, [1:   6]) = [  9.62931E-03 0.00014  7.69326E-03 0.00011  7.30302E-02 0.00030 ];
ELAXS                     (idx, [1:   6]) = [  2.83347E-01 3.3E-05  2.81550E-01 3.4E-05  3.42215E-01 8.2E-05 ];
INELAXS                   (idx, [1:   6]) = [  1.27067E-02 0.00012  1.30947E-02 0.00012  1.69165E-17 0.00036 ];
SCATTXS                   (idx, [1:   6]) = [  2.96054E-01 2.9E-05  2.94644E-01 3.0E-05  3.42215E-01 8.2E-05 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.96087E-01 2.9E-05  2.94679E-01 3.0E-05  3.42215E-01 8.2E-05 ];
REMXS                     (idx, [1:   6]) = [  9.62903E-03 0.00027  9.90292E-03 0.00027  7.29783E-02 0.00044 ];
NUBAR                     (idx, [1:   6]) = [  2.50876E+00 1.3E-05  2.51842E+00 1.9E-05  2.48805E+00 1.1E-07 ];
NSF                       (idx, [1:   6]) = [  1.12940E-02 0.00017  7.96415E-03 9.6E-05  1.20338E-01 0.00032 ];
RECIPVEL                  (idx, [1:   6]) = [  9.99114E-09 0.00037  4.92506E-09 0.00016  1.75885E-07 0.00052 ];
FISSE                     (idx, [1:   6]) = [  1.99180E+02 1.5E-07  1.99136E+02 1.8E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 2.1E-07  1.08292E-06 0.19760 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 2.0E-07  9.12630E-07 0.21604 ];
CHID                      (idx, [1:   4]) = [  9.99950E-01 2.5E-05  5.03549E-05 0.50019 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.92505E-01 3.4E-06  0.00000E+00 0.0E+00  7.49466E-03 0.00046  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.92435E-01 3.3E-05  0.00000E+00 0.0E+00  2.20825E-03 0.00046  3.42267E-01 0.00012 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.92623E-01 3.5E-06  0.00000E+00 0.0E+00  7.49466E-03 0.00046  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.92469E-01 3.3E-05  0.00000E+00 0.0E+00  2.20825E-03 0.00046  3.42267E-01 0.00012 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.96054E-01 3.2E-05  2.94643E-01 3.3E-05  3.42267E-01 0.00012 ];
SCATT1                    (idx, [1:   6]) = [  5.63835E-02 0.00012  5.64798E-02 0.00012  5.32282E-02 0.00080 ];
SCATT2                    (idx, [1:   6]) = [  2.34686E-02 0.00023  2.36139E-02 0.00024  1.87095E-02 0.00185 ];
SCATT3                    (idx, [1:   6]) = [  4.55256E-03 0.00108  4.66871E-03 0.00107  7.48345E-04 0.03723 ];
SCATT4                    (idx, [1:   6]) = [  1.00665E-03 0.00410  1.13119E-03 0.00375 -3.07166E-03 0.00808 ];
SCATT5                    (idx, [1:   6]) = [  1.15878E-03 0.00318  1.21147E-03 0.00307 -5.66256E-04 0.04097 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.49333E-01 4.8E-05  2.45892E-01 4.8E-05  3.62017E-01 0.00018 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.33690E+00 4.8E-05  1.35561E+00 4.8E-05  9.20796E-01 0.00018 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.90450E-01 0.00013  1.91689E-01 0.00013  1.55520E-01 0.00082 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.16876E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  1.21991E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  1.08513E-06 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.15694E-01 0.0E+00  2.13110E-01 0.0E+00  3.57649E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.54540E+00 0.0E+00  1.56414E+00 0.0E+00  9.32012E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98269 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '325' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  2.29521E+18 0.00015  2.23487E+18 0.00015  6.03387E+16 0.00049 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  3.01554E-01 3.0E-05  2.98748E-01 3.1E-05  4.05489E-01 0.00012 ];
FISSXS                    (idx, [1:   6]) = [  4.27648E-03 0.00016  3.12511E-03 9.2E-05  4.69229E-02 0.00032 ];
CAPTXS                    (idx, [1:   6]) = [  5.04039E-03 0.00015  4.51859E-03 0.00014  2.43688E-02 0.00058 ];
ABSXS                     (idx, [1:   6]) = [  9.31688E-03 0.00013  7.64370E-03 0.00011  7.12917E-02 0.00032 ];
RABSXS                    (idx, [1:   6]) = [  9.28450E-03 0.00013  7.61045E-03 0.00011  7.12917E-02 0.00032 ];
ELAXS                     (idx, [1:   6]) = [  2.79696E-01 3.3E-05  2.78224E-01 3.4E-05  3.34198E-01 9.5E-05 ];
INELAXS                   (idx, [1:   6]) = [  1.25413E-02 0.00011  1.28799E-02 0.00011  1.45739E-17 0.00041 ];
SCATTXS                   (idx, [1:   6]) = [  2.92237E-01 2.9E-05  2.91104E-01 3.0E-05  3.34198E-01 9.5E-05 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.92269E-01 2.9E-05  2.91137E-01 3.0E-05  3.34198E-01 9.5E-05 ];
REMXS                     (idx, [1:   6]) = [  9.28244E-03 0.00028  9.52804E-03 0.00028  7.12985E-02 0.00043 ];
NUBAR                     (idx, [1:   6]) = [  2.50949E+00 1.3E-05  2.51817E+00 1.8E-05  2.48807E+00 1.2E-07 ];
NSF                       (idx, [1:   6]) = [  1.07318E-02 0.00016  7.86955E-03 9.2E-05  1.16748E-01 0.00032 ];
RECIPVEL                  (idx, [1:   6]) = [  9.11012E-09 0.00037  4.84054E-09 0.00015  1.67245E-07 0.00053 ];
FISSE                     (idx, [1:   6]) = [  1.99178E+02 1.5E-07  1.99139E+02 1.8E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 2.2E-07  1.12279E-06 0.19366 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 1.9E-07  8.23070E-07 0.22736 ];
CHID                      (idx, [1:   4]) = [  9.99912E-01 3.3E-05  8.82621E-05 0.37883 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.93405E-01 3.2E-06  0.00000E+00 0.0E+00  6.59481E-03 0.00048  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.89187E-01 3.3E-05  0.00000E+00 0.0E+00  1.91979E-03 0.00048  3.34191E-01 0.00013 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.93519E-01 3.2E-06  0.00000E+00 0.0E+00  6.59481E-03 0.00048  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.89220E-01 3.3E-05  0.00000E+00 0.0E+00  1.91979E-03 0.00048  3.34191E-01 0.00013 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.92239E-01 3.2E-05  2.91107E-01 3.3E-05  3.34191E-01 0.00013 ];
SCATT1                    (idx, [1:   6]) = [  5.37750E-02 0.00013  5.39179E-02 0.00013  4.84810E-02 0.00088 ];
SCATT2                    (idx, [1:   6]) = [  2.23609E-02 0.00024  2.25096E-02 0.00024  1.68491E-02 0.00210 ];
SCATT3                    (idx, [1:   6]) = [  4.42793E-03 0.00102  4.52965E-03 0.00101  6.59381E-04 0.04589 ];
SCATT4                    (idx, [1:   6]) = [  1.09310E-03 0.00383  1.19746E-03 0.00356 -2.77269E-03 0.00948 ];
SCATT5                    (idx, [1:   6]) = [  1.12351E-03 0.00326  1.16757E-03 0.00319 -5.08484E-04 0.04578 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.47779E-01 4.9E-05  2.44830E-01 4.9E-05  3.57008E-01 0.00019 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.34529E+00 4.9E-05  1.36149E+00 4.9E-05  9.33721E-01 0.00019 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.84010E-01 0.00014  1.85217E-01 0.00014  1.45074E-01 0.00091 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.15211E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  1.05359E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  1.12587E-06 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.15204E-01 0.0E+00  2.12959E-01 0.0E+00  3.53019E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.54892E+00 0.0E+00  1.56525E+00 0.0E+00  9.44237E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98269 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '326' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  2.37582E+18 0.00014  2.31927E+18 0.00014  5.65418E+16 0.00051 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  2.98344E-01 3.0E-05  2.95911E-01 3.0E-05  3.98148E-01 0.00012 ];
FISSXS                    (idx, [1:   6]) = [  4.11288E-03 0.00016  3.09426E-03 8.9E-05  4.58965E-02 0.00032 ];
CAPTXS                    (idx, [1:   6]) = [  4.94993E-03 0.00014  4.48137E-03 0.00013  2.41712E-02 0.00059 ];
ABSXS                     (idx, [1:   6]) = [  9.06281E-03 0.00013  7.57564E-03 0.00010  7.00677E-02 0.00033 ];
RABSXS                    (idx, [1:   6]) = [  9.03134E-03 0.00013  7.54340E-03 0.00010  7.00677E-02 0.00033 ];
ELAXS                     (idx, [1:   6]) = [  2.76872E-01 3.2E-05  2.75623E-01 3.3E-05  3.28080E-01 0.00010 ];
INELAXS                   (idx, [1:   6]) = [  1.24092E-02 0.00011  1.27118E-02 0.00011  1.46365E-17 0.00041 ];
SCATTXS                   (idx, [1:   6]) = [  2.89281E-01 2.9E-05  2.88335E-01 2.9E-05  3.28080E-01 0.00010 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.89312E-01 2.9E-05  2.88367E-01 2.9E-05  3.28080E-01 0.00010 ];
REMXS                     (idx, [1:   6]) = [  9.03312E-03 0.00028  9.24871E-03 0.00028  7.01007E-02 0.00049 ];
NUBAR                     (idx, [1:   6]) = [  2.50997E+00 1.4E-05  2.51788E+00 1.8E-05  2.48809E+00 1.2E-07 ];
NSF                       (idx, [1:   6]) = [  1.03232E-02 0.00016  7.79097E-03 9.1E-05  1.14195E-01 0.00032 ];
RECIPVEL                  (idx, [1:   6]) = [  8.49080E-09 0.00037  4.77018E-09 0.00015  1.61100E-07 0.00054 ];
FISSE                     (idx, [1:   6]) = [  1.99177E+02 1.5E-07  1.99142E+02 1.7E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 2.2E-07  1.17467E-06 0.18994 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 1.7E-07  6.52730E-07 0.25640 ];
CHID                      (idx, [1:   4]) = [  9.99843E-01 4.6E-05  1.57028E-04 0.29037 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.94090E-01 3.0E-06  0.00000E+00 0.0E+00  5.91040E-03 0.00050  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.86630E-01 3.2E-05  0.00000E+00 0.0E+00  1.70417E-03 0.00050  3.28047E-01 0.00014 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.94201E-01 3.0E-06  0.00000E+00 0.0E+00  5.91040E-03 0.00050  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.86662E-01 3.2E-05  0.00000E+00 0.0E+00  1.70417E-03 0.00050  3.28047E-01 0.00014 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.89279E-01 3.1E-05  2.88334E-01 3.2E-05  3.28047E-01 0.00014 ];
SCATT1                    (idx, [1:   6]) = [  5.17351E-02 0.00013  5.19070E-02 0.00013  4.46822E-02 0.00101 ];
SCATT2                    (idx, [1:   6]) = [  2.15020E-02 0.00024  2.16497E-02 0.00025  1.54422E-02 0.00228 ];
SCATT3                    (idx, [1:   6]) = [  4.34358E-03 0.00102  4.43563E-03 0.00101  5.67671E-04 0.05444 ];
SCATT4                    (idx, [1:   6]) = [  1.15494E-03 0.00348  1.24516E-03 0.00328 -2.54659E-03 0.01056 ];
SCATT5                    (idx, [1:   6]) = [  1.09084E-03 0.00332  1.12874E-03 0.00322 -4.63635E-04 0.05113 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.46609E-01 4.7E-05  2.44004E-01 4.8E-05  3.53466E-01 0.00021 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.35167E+00 4.7E-05  1.36610E+00 4.8E-05  9.43083E-01 0.00021 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.78841E-01 0.00014  1.80024E-01 0.00014  1.36213E-01 0.00105 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.13964E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  9.36380E-04 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  1.17324E-06 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.14832E-01 0.0E+00  2.12830E-01 0.0E+00  3.49737E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.55160E+00 0.0E+00  1.56620E+00 0.0E+00  9.53098E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98269 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '327' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  2.42012E+18 0.00014  2.36712E+18 0.00014  5.29970E+16 0.00052 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  2.95919E-01 2.9E-05  2.93757E-01 3.0E-05  3.92487E-01 0.00014 ];
FISSXS                    (idx, [1:   6]) = [  3.98860E-03 0.00016  3.06892E-03 8.6E-05  4.50674E-02 0.00036 ];
CAPTXS                    (idx, [1:   6]) = [  4.87825E-03 0.00014  4.45018E-03 0.00013  2.40001E-02 0.00063 ];
ABSXS                     (idx, [1:   6]) = [  8.86685E-03 0.00012  7.51910E-03 0.00010  6.90675E-02 0.00036 ];
RABSXS                    (idx, [1:   6]) = [  8.83614E-03 0.00013  7.48771E-03 0.00010  6.90675E-02 0.00036 ];
ELAXS                     (idx, [1:   6]) = [  2.74751E-01 3.2E-05  2.73662E-01 3.2E-05  3.23420E-01 0.00012 ];
INELAXS                   (idx, [1:   6]) = [  1.23006E-02 0.00012  1.25760E-02 0.00011  1.45959E-17 0.00042 ];
SCATTXS                   (idx, [1:   6]) = [  2.87052E-01 2.8E-05  2.86238E-01 2.9E-05  3.23420E-01 0.00012 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.87083E-01 2.8E-05  2.86269E-01 2.9E-05  3.23420E-01 0.00012 ];
REMXS                     (idx, [1:   6]) = [  8.83491E-03 0.00030  9.02998E-03 0.00029  6.90724E-02 0.00050 ];
NUBAR                     (idx, [1:   6]) = [  2.51041E+00 1.3E-05  2.51774E+00 1.8E-05  2.48810E+00 1.2E-07 ];
NSF                       (idx, [1:   6]) = [  1.00130E-02 0.00016  7.72674E-03 8.8E-05  1.12132E-01 0.00036 ];
RECIPVEL                  (idx, [1:   6]) = [  8.03526E-09 0.00035  4.71218E-09 0.00015  1.56456E-07 0.00054 ];
FISSE                     (idx, [1:   6]) = [  1.99176E+02 1.5E-07  1.99144E+02 1.7E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 2.5E-07  1.35644E-06 0.18249 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 2.2E-07  1.00915E-06 0.21490 ];
CHID                      (idx, [1:   4]) = [  9.99902E-01 3.5E-05  9.78465E-05 0.35371 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.94608E-01 2.9E-06  5.79912E-08 1.00000  5.39247E-03 0.00053  1.00000E+00 5.8E-08 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.84696E-01 3.1E-05  1.87310E-08 1.00000  1.54354E-03 0.00053  3.23415E-01 0.00015 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.94717E-01 2.9E-06  5.79912E-08 1.00000  5.39247E-03 0.00053  1.00000E+00 5.8E-08 ];
GPRODXS                   (idx, [1:   8]) = [  2.84727E-01 3.1E-05  1.87310E-08 1.00000  1.54354E-03 0.00053  3.23415E-01 0.00015 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.87053E-01 3.0E-05  2.86239E-01 3.1E-05  3.23415E-01 0.00015 ];
SCATT1                    (idx, [1:   6]) = [  5.01696E-02 0.00014  5.03558E-02 0.00014  4.18501E-02 0.00108 ];
SCATT2                    (idx, [1:   6]) = [  2.08268E-02 0.00026  2.09713E-02 0.00026  1.43706E-02 0.00250 ];
SCATT3                    (idx, [1:   6]) = [  4.27957E-03 0.00100  4.36355E-03 0.00099  5.27793E-04 0.05810 ];
SCATT4                    (idx, [1:   6]) = [  1.20767E-03 0.00326  1.28762E-03 0.00308 -2.36217E-03 0.01159 ];
SCATT5                    (idx, [1:   6]) = [  1.07295E-03 0.00325  1.10634E-03 0.00321 -4.18285E-04 0.06176 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.45749E-01 4.5E-05  2.43401E-01 4.6E-05  3.50637E-01 0.00022 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.35640E+00 4.5E-05  1.36948E+00 4.6E-05  9.50697E-01 0.00022 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.74775E-01 0.00014  1.75922E-01 0.00014  1.29406E-01 0.00111 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.12884E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  8.42303E-04 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  1.36658E-06 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.14594E-01 0.0E+00  2.12775E-01 0.0E+00  3.47106E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.55332E+00 0.0E+00  1.56660E+00 0.0E+00  9.60322E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98268 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '328' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  2.43332E+18 0.00014  2.38378E+18 0.00014  4.95427E+16 0.00054 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  2.94000E-01 3.1E-05  2.92047E-01 3.1E-05  3.87986E-01 0.00014 ];
FISSXS                    (idx, [1:   6]) = [  3.89002E-03 0.00015  3.04752E-03 8.9E-05  4.44288E-02 0.00036 ];
CAPTXS                    (idx, [1:   6]) = [  4.81891E-03 0.00013  4.42330E-03 0.00013  2.38562E-02 0.00063 ];
ABSXS                     (idx, [1:   6]) = [  8.70894E-03 0.00012  7.47081E-03 0.00010  6.82851E-02 0.00036 ];
RABSXS                    (idx, [1:   6]) = [  8.67880E-03 0.00012  7.44005E-03 0.00010  6.82851E-02 0.00036 ];
ELAXS                     (idx, [1:   6]) = [  2.73077E-01 3.3E-05  2.72108E-01 3.4E-05  3.19701E-01 0.00012 ];
INELAXS                   (idx, [1:   6]) = [  1.22147E-02 0.00011  1.24686E-02 0.00011  1.45144E-17 0.00044 ];
SCATTXS                   (idx, [1:   6]) = [  2.85292E-01 3.0E-05  2.84577E-01 3.0E-05  3.19701E-01 0.00012 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.85322E-01 3.0E-05  2.84607E-01 3.0E-05  3.19701E-01 0.00012 ];
REMXS                     (idx, [1:   6]) = [  8.68033E-03 0.00031  8.85875E-03 0.00030  6.82904E-02 0.00052 ];
NUBAR                     (idx, [1:   6]) = [  2.51071E+00 1.3E-05  2.51756E+00 1.7E-05  2.48811E+00 1.3E-07 ];
NSF                       (idx, [1:   6]) = [  9.76673E-03 0.00015  7.67230E-03 9.1E-05  1.10544E-01 0.00036 ];
RECIPVEL                  (idx, [1:   6]) = [  7.68447E-09 0.00034  4.66166E-09 0.00015  1.53126E-07 0.00056 ];
FISSE                     (idx, [1:   6]) = [  1.99175E+02 1.5E-07  1.99145E+02 1.7E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 2.7E-07  1.39161E-06 0.19386 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 2.4E-07  1.03553E-06 0.23231 ];
CHID                      (idx, [1:   4]) = [  9.99892E-01 3.8E-05  1.07996E-04 0.35485 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.95020E-01 2.7E-06  0.00000E+00 0.0E+00  4.97990E-03 0.00055  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.83158E-01 3.3E-05  0.00000E+00 0.0E+00  1.41715E-03 0.00055  3.19696E-01 0.00015 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.95128E-01 2.8E-06  0.00000E+00 0.0E+00  4.97990E-03 0.00055  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.83189E-01 3.3E-05  0.00000E+00 0.0E+00  1.41715E-03 0.00055  3.19696E-01 0.00015 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.85290E-01 3.3E-05  2.84575E-01 3.3E-05  3.19696E-01 0.00015 ];
SCATT1                    (idx, [1:   6]) = [  4.89200E-02 0.00013  4.91134E-02 0.00014  3.96127E-02 0.00119 ];
SCATT2                    (idx, [1:   6]) = [  2.02935E-02 0.00025  2.04348E-02 0.00025  1.34965E-02 0.00287 ];
SCATT3                    (idx, [1:   6]) = [  4.21218E-03 0.00102  4.29118E-03 0.00101  4.11052E-04 0.07871 ];
SCATT4                    (idx, [1:   6]) = [  1.23136E-03 0.00306  1.30409E-03 0.00292 -2.26761E-03 0.01265 ];
SCATT5                    (idx, [1:   6]) = [  1.05377E-03 0.00333  1.08426E-03 0.00327 -4.12874E-04 0.06223 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.45080E-01 4.7E-05  2.42934E-01 4.8E-05  3.48374E-01 0.00022 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.36010E+00 4.7E-05  1.37212E+00 4.8E-05  9.56874E-01 0.00022 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.71475E-01 0.00014  1.72585E-01 0.00014  1.23913E-01 0.00122 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.12112E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  7.75610E-04 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  1.39139E-06 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.14440E-01 0.0E+00  2.12766E-01 0.0E+00  3.45003E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.55443E+00 0.0E+00  1.56666E+00 0.0E+00  9.66176E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98268 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '329' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  2.41727E+18 0.00014  2.37106E+18 0.00014  4.62114E+16 0.00054 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  2.92441E-01 3.1E-05  2.90646E-01 3.1E-05  3.84537E-01 0.00016 ];
FISSXS                    (idx, [1:   6]) = [  3.81034E-03 0.00015  3.02871E-03 8.9E-05  4.39157E-02 0.00038 ];
CAPTXS                    (idx, [1:   6]) = [  4.77167E-03 0.00014  4.40100E-03 0.00013  2.37923E-02 0.00070 ];
ABSXS                     (idx, [1:   6]) = [  8.58200E-03 0.00012  7.42972E-03 0.00010  6.77080E-02 0.00038 ];
RABSXS                    (idx, [1:   6]) = [  8.55233E-03 0.00012  7.39947E-03 0.00011  6.77080E-02 0.00038 ];
ELAXS                     (idx, [1:   6]) = [  2.71721E-01 3.4E-05  2.70842E-01 3.4E-05  3.16829E-01 0.00013 ];
INELAXS                   (idx, [1:   6]) = [  1.21377E-02 0.00012  1.23743E-02 0.00012  1.50702E-17 0.00048 ];
SCATTXS                   (idx, [1:   6]) = [  2.83859E-01 3.0E-05  2.83216E-01 3.1E-05  3.16829E-01 0.00013 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.83888E-01 3.0E-05  2.83247E-01 3.1E-05  3.16829E-01 0.00013 ];
REMXS                     (idx, [1:   6]) = [  8.54912E-03 0.00030  8.71468E-03 0.00030  6.77007E-02 0.00054 ];
NUBAR                     (idx, [1:   6]) = [  2.51098E+00 1.4E-05  2.51745E+00 1.8E-05  2.48812E+00 1.4E-07 ];
NSF                       (idx, [1:   6]) = [  9.56768E-03 0.00015  7.62464E-03 9.0E-05  1.09268E-01 0.00038 ];
RECIPVEL                  (idx, [1:   6]) = [  7.39954E-09 0.00033  4.61844E-09 0.00015  1.50094E-07 0.00059 ];
FISSE                     (idx, [1:   6]) = [  1.99175E+02 1.5E-07  1.99147E+02 1.7E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 2.3E-07  9.22126E-07 0.25328 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 1.9E-07  5.56028E-07 0.33283 ];
CHID                      (idx, [1:   4]) = [  9.99894E-01 3.8E-05  1.06452E-04 0.35408 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.95345E-01 2.5E-06  0.00000E+00 0.0E+00  4.65451E-03 0.00052  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.81901E-01 3.3E-05  0.00000E+00 0.0E+00  1.31825E-03 0.00052  3.16837E-01 0.00017 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.95453E-01 2.5E-06  0.00000E+00 0.0E+00  4.65451E-03 0.00052  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.81931E-01 3.3E-05  0.00000E+00 0.0E+00  1.31825E-03 0.00052  3.16837E-01 0.00017 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.83862E-01 3.2E-05  2.83219E-01 3.3E-05  3.16837E-01 0.00017 ];
SCATT1                    (idx, [1:   6]) = [  4.79295E-02 0.00014  4.81299E-02 0.00014  3.76451E-02 0.00129 ];
SCATT2                    (idx, [1:   6]) = [  1.98692E-02 0.00027  2.00081E-02 0.00027  1.27432E-02 0.00308 ];
SCATT3                    (idx, [1:   6]) = [  4.16676E-03 0.00102  4.24084E-03 0.00101  3.65199E-04 0.08641 ];
SCATT4                    (idx, [1:   6]) = [  1.26233E-03 0.00299  1.32843E-03 0.00287 -2.13000E-03 0.01393 ];
SCATT5                    (idx, [1:   6]) = [  1.03614E-03 0.00340  1.06335E-03 0.00335 -3.60755E-04 0.07405 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.44511E-01 4.9E-05  2.42516E-01 5.0E-05  3.46892E-01 0.00024 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.36327E+00 4.9E-05  1.37448E+00 5.0E-05  9.60969E-01 0.00024 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.68848E-01 0.00015  1.69939E-01 0.00015  1.18822E-01 0.00132 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.11419E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  7.18927E-04 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  9.22444E-07 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.14276E-01 0.0E+00  2.12715E-01 0.0E+00  3.43662E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.55562E+00 0.0E+00  1.56704E+00 0.0E+00  9.69946E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98268 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '330' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  2.37579E+18 0.00015  2.33274E+18 0.00015  4.30558E+16 0.00059 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  2.91198E-01 3.1E-05  2.89529E-01 3.1E-05  3.81628E-01 0.00016 ];
FISSXS                    (idx, [1:   6]) = [  3.74612E-03 0.00015  3.01289E-03 8.9E-05  4.34743E-02 0.00040 ];
CAPTXS                    (idx, [1:   6]) = [  4.73223E-03 0.00013  4.38179E-03 0.00012  2.37214E-02 0.00068 ];
ABSXS                     (idx, [1:   6]) = [  8.47835E-03 0.00012  7.39468E-03 1.0E-04  6.71957E-02 0.00038 ];
RABSXS                    (idx, [1:   6]) = [  8.44898E-03 0.00012  7.36477E-03 1.0E-04  6.71957E-02 0.00038 ];
ELAXS                     (idx, [1:   6]) = [  2.70641E-01 3.4E-05  2.69833E-01 3.4E-05  3.14433E-01 0.00014 ];
INELAXS                   (idx, [1:   6]) = [  1.20792E-02 0.00012  1.23021E-02 0.00012  1.49517E-17 0.00045 ];
SCATTXS                   (idx, [1:   6]) = [  2.82720E-01 3.0E-05  2.82135E-01 3.1E-05  3.14433E-01 0.00014 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.82749E-01 3.0E-05  2.82165E-01 3.1E-05  3.14433E-01 0.00014 ];
REMXS                     (idx, [1:   6]) = [  8.44567E-03 0.00031  8.59974E-03 0.00031  6.71762E-02 0.00059 ];
NUBAR                     (idx, [1:   6]) = [  2.51115E+00 1.4E-05  2.51728E+00 1.8E-05  2.48813E+00 1.4E-07 ];
NSF                       (idx, [1:   6]) = [  9.40706E-03 0.00015  7.58429E-03 9.0E-05  1.08170E-01 0.00040 ];
RECIPVEL                  (idx, [1:   6]) = [  7.17240E-09 0.00034  4.58091E-09 0.00016  1.47575E-07 0.00059 ];
FISSE                     (idx, [1:   6]) = [  1.99174E+02 1.5E-07  1.99148E+02 1.7E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 2.4E-07  1.19403E-06 0.19759 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 1.9E-07  7.66554E-07 0.24813 ];
CHID                      (idx, [1:   4]) = [  9.99872E-01 4.3E-05  1.27503E-04 0.33358 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.95612E-01 2.5E-06  7.51258E-08 1.00000  4.38754E-03 0.00057  1.00000E+00 7.5E-08 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.80900E-01 3.3E-05  2.36853E-08 1.00000  1.23789E-03 0.00057  3.14452E-01 0.00018 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.95718E-01 2.5E-06  7.51258E-08 1.00000  4.38754E-03 0.00057  1.00000E+00 7.5E-08 ];
GPRODXS                   (idx, [1:   8]) = [  2.80930E-01 3.3E-05  2.36853E-08 1.00000  1.23789E-03 0.00057  3.14452E-01 0.00018 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.82723E-01 3.2E-05  2.82138E-01 3.3E-05  3.14452E-01 0.00018 ];
SCATT1                    (idx, [1:   6]) = [  4.71049E-02 0.00014  4.73055E-02 0.00014  3.62351E-02 0.00143 ];
SCATT2                    (idx, [1:   6]) = [  1.95208E-02 0.00025  1.96551E-02 0.00025  1.22454E-02 0.00325 ];
SCATT3                    (idx, [1:   6]) = [  4.13069E-03 0.00108  4.19939E-03 0.00108  4.08195E-04 0.08167 ];
SCATT4                    (idx, [1:   6]) = [  1.28572E-03 0.00307  1.34608E-03 0.00296 -1.98364E-03 0.01526 ];
SCATT5                    (idx, [1:   6]) = [  1.03026E-03 0.00334  1.05593E-03 0.00328 -3.60373E-04 0.07535 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.44093E-01 4.7E-05  2.42224E-01 4.7E-05  3.45393E-01 0.00025 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.36560E+00 4.7E-05  1.37614E+00 4.7E-05  9.65145E-01 0.00025 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.66612E-01 0.00014  1.67668E-01 0.00014  1.15240E-01 0.00147 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.10868E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  6.74799E-04 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  1.19425E-06 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.14198E-01 0.0E+00  2.12729E-01 0.0E+00  3.42222E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.55619E+00 0.0E+00  1.56694E+00 0.0E+00  9.74028E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98268 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '331' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  2.31031E+18 0.00015  2.27038E+18 0.00015  3.99315E+16 0.00062 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  2.90180E-01 3.2E-05  2.88614E-01 3.2E-05  3.79187E-01 0.00018 ];
FISSXS                    (idx, [1:   6]) = [  3.69158E-03 0.00016  2.99910E-03 9.4E-05  4.30660E-02 0.00041 ];
CAPTXS                    (idx, [1:   6]) = [  4.69794E-03 0.00014  4.36461E-03 0.00013  2.36524E-02 0.00076 ];
ABSXS                     (idx, [1:   6]) = [  8.38951E-03 0.00013  7.36371E-03 0.00011  6.67184E-02 0.00043 ];
RABSXS                    (idx, [1:   6]) = [  8.36049E-03 0.00013  7.33417E-03 0.00011  6.67184E-02 0.00043 ];
ELAXS                     (idx, [1:   6]) = [  2.69762E-01 3.4E-05  2.69011E-01 3.5E-05  3.12468E-01 0.00015 ];
INELAXS                   (idx, [1:   6]) = [  1.20281E-02 0.00012  1.22397E-02 0.00012  1.49921E-17 0.00049 ];
SCATTXS                   (idx, [1:   6]) = [  2.81790E-01 3.1E-05  2.81251E-01 3.1E-05  3.12468E-01 0.00015 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.81819E-01 3.1E-05  2.81280E-01 3.1E-05  3.12468E-01 0.00015 ];
REMXS                     (idx, [1:   6]) = [  8.36177E-03 0.00035  8.50757E-03 0.00034  6.66987E-02 0.00061 ];
NUBAR                     (idx, [1:   6]) = [  2.51141E+00 1.4E-05  2.51729E+00 1.8E-05  2.48813E+00 1.5E-07 ];
NSF                       (idx, [1:   6]) = [  9.27108E-03 0.00016  7.54959E-03 9.6E-05  1.07154E-01 0.00041 ];
RECIPVEL                  (idx, [1:   6]) = [  6.98775E-09 0.00035  4.54774E-09 0.00016  1.45714E-07 0.00064 ];
FISSE                     (idx, [1:   6]) = [  1.99173E+02 1.6E-07  1.99148E+02 1.7E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 2.2E-07  9.95331E-07 0.22149 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 1.9E-07  6.98963E-07 0.26554 ];
CHID                      (idx, [1:   4]) = [  9.99916E-01 3.4E-05  8.37314E-05 0.41157 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.95834E-01 2.6E-06  0.00000E+00 0.0E+00  4.16582E-03 0.00062  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.80077E-01 3.4E-05  0.00000E+00 0.0E+00  1.17163E-03 0.00062  3.12488E-01 0.00019 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.95939E-01 2.6E-06  0.00000E+00 0.0E+00  4.16582E-03 0.00062  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.80107E-01 3.4E-05  0.00000E+00 0.0E+00  1.17163E-03 0.00062  3.12488E-01 0.00019 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.81789E-01 3.4E-05  2.81249E-01 3.4E-05  3.12488E-01 0.00019 ];
SCATT1                    (idx, [1:   6]) = [  4.64228E-02 0.00014  4.66232E-02 0.00015  3.50244E-02 0.00151 ];
SCATT2                    (idx, [1:   6]) = [  1.92302E-02 0.00028  1.93610E-02 0.00028  1.17930E-02 0.00345 ];
SCATT3                    (idx, [1:   6]) = [  4.10455E-03 0.00111  4.16933E-03 0.00110  4.21256E-04 0.08499 ];
SCATT4                    (idx, [1:   6]) = [  1.30300E-03 0.00294  1.36030E-03 0.00284 -1.95470E-03 0.01568 ];
SCATT5                    (idx, [1:   6]) = [  1.02082E-03 0.00345  1.04516E-03 0.00337 -3.61954E-04 0.07678 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.43757E-01 4.8E-05  2.41991E-01 4.9E-05  3.44162E-01 0.00027 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.36749E+00 4.8E-05  1.37746E+00 4.9E-05  9.68607E-01 0.00027 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.64743E-01 0.00015  1.65772E-01 0.00015  1.12091E-01 0.00155 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.10498E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  6.44108E-04 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  9.95643E-07 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.14124E-01 0.0E+00  2.12731E-01 0.0E+00  3.41096E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.55673E+00 0.0E+00  1.56692E+00 0.0E+00  9.77241E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79223E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98268 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '332' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  2.22294E+18 0.00016  2.18614E+18 0.00016  3.68039E+16 0.00068 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  2.89321E-01 3.1E-05  2.87843E-01 3.2E-05  3.77135E-01 0.00019 ];
FISSXS                    (idx, [1:   6]) = [  3.64676E-03 0.00016  2.98775E-03 9.2E-05  4.27941E-02 0.00044 ];
CAPTXS                    (idx, [1:   6]) = [  4.66866E-03 0.00014  4.35033E-03 0.00013  2.35807E-02 0.00077 ];
ABSXS                     (idx, [1:   6]) = [  8.31542E-03 0.00013  7.33808E-03 0.00011  6.63748E-02 0.00044 ];
RABSXS                    (idx, [1:   6]) = [  8.28671E-03 0.00013  7.30889E-03 0.00011  6.63748E-02 0.00044 ];
ELAXS                     (idx, [1:   6]) = [  2.69021E-01 3.4E-05  2.68319E-01 3.5E-05  3.10760E-01 0.00016 ];
INELAXS                   (idx, [1:   6]) = [  1.19844E-02 0.00012  1.21861E-02 0.00012  1.48825E-17 0.00051 ];
SCATTXS                   (idx, [1:   6]) = [  2.81006E-01 3.1E-05  2.80505E-01 3.1E-05  3.10760E-01 0.00016 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.81035E-01 3.1E-05  2.80534E-01 3.1E-05  3.10760E-01 0.00016 ];
REMXS                     (idx, [1:   6]) = [  8.28477E-03 0.00033  8.42259E-03 0.00033  6.63951E-02 0.00066 ];
NUBAR                     (idx, [1:   6]) = [  2.51157E+00 1.5E-05  2.51722E+00 1.8E-05  2.48814E+00 1.5E-07 ];
NSF                       (idx, [1:   6]) = [  9.15910E-03 0.00016  7.52084E-03 9.4E-05  1.06478E-01 0.00044 ];
RECIPVEL                  (idx, [1:   6]) = [  6.83384E-09 0.00037  4.52012E-09 0.00016  1.44262E-07 0.00067 ];
FISSE                     (idx, [1:   6]) = [  1.99173E+02 1.6E-07  1.99149E+02 1.8E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 2.0E-07  7.37879E-07 0.26553 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 1.8E-07  5.83464E-07 0.30001 ];
CHID                      (idx, [1:   4]) = [  9.99956E-01 2.5E-05  4.35201E-05 0.57705 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.96022E-01 2.6E-06  0.00000E+00 0.0E+00  3.97811E-03 0.00065  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.79391E-01 3.4E-05  0.00000E+00 0.0E+00  1.11589E-03 0.00065  3.10740E-01 0.00021 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.96126E-01 2.6E-06  0.00000E+00 0.0E+00  3.97811E-03 0.00065  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.79421E-01 3.4E-05  0.00000E+00 0.0E+00  1.11589E-03 0.00065  3.10740E-01 0.00021 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.81008E-01 3.4E-05  2.80507E-01 3.4E-05  3.10740E-01 0.00021 ];
SCATT1                    (idx, [1:   6]) = [  4.58648E-02 0.00015  4.60653E-02 0.00015  3.39495E-02 0.00163 ];
SCATT2                    (idx, [1:   6]) = [  1.89840E-02 0.00029  1.91118E-02 0.00029  1.13945E-02 0.00372 ];
SCATT3                    (idx, [1:   6]) = [  4.06727E-03 0.00112  4.13028E-03 0.00112  3.22380E-04 0.11251 ];
SCATT4                    (idx, [1:   6]) = [  1.32221E-03 0.00304  1.37643E-03 0.00295 -1.89881E-03 0.01692 ];
SCATT5                    (idx, [1:   6]) = [  1.02060E-03 0.00340  1.04323E-03 0.00334 -3.23095E-04 0.09017 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.43456E-01 4.9E-05  2.41778E-01 5.0E-05  3.43185E-01 0.00029 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.36917E+00 4.9E-05  1.37868E+00 5.0E-05  9.71373E-01 0.00029 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.63216E-01 0.00015  1.64222E-01 0.00015  1.09264E-01 0.00168 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.10122E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  6.14764E-04 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  7.33448E-07 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.14056E-01 0.0E+00  2.12728E-01 0.0E+00  3.40167E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.55722E+00 0.0E+00  1.56694E+00 0.0E+00  9.79911E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98268 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '333' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  2.11663E+18 0.00017  2.08276E+18 0.00017  3.38675E+16 0.00068 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  2.88615E-01 3.2E-05  2.87204E-01 3.2E-05  3.75418E-01 0.00020 ];
FISSXS                    (idx, [1:   6]) = [  3.60969E-03 0.00016  2.97745E-03 9.2E-05  4.24932E-02 0.00046 ];
CAPTXS                    (idx, [1:   6]) = [  4.64434E-03 0.00014  4.33741E-03 0.00013  2.35223E-02 0.00080 ];
ABSXS                     (idx, [1:   6]) = [  8.25403E-03 0.00013  7.31486E-03 0.00010  6.60155E-02 0.00045 ];
RABSXS                    (idx, [1:   6]) = [  8.22546E-03 0.00013  7.28582E-03 0.00011  6.60155E-02 0.00045 ];
ELAXS                     (idx, [1:   6]) = [  2.68412E-01 3.5E-05  2.67746E-01 3.5E-05  3.09402E-01 0.00017 ];
INELAXS                   (idx, [1:   6]) = [  1.19492E-02 0.00012  1.21435E-02 0.00012  1.48453E-17 0.00053 ];
SCATTXS                   (idx, [1:   6]) = [  2.80361E-01 3.1E-05  2.79889E-01 3.2E-05  3.09402E-01 0.00017 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.80390E-01 3.1E-05  2.79918E-01 3.2E-05  3.09402E-01 0.00017 ];
REMXS                     (idx, [1:   6]) = [  8.22376E-03 0.00035  8.35636E-03 0.00034  6.60633E-02 0.00066 ];
NUBAR                     (idx, [1:   6]) = [  2.51172E+00 1.5E-05  2.51720E+00 1.8E-05  2.48814E+00 1.6E-07 ];
NSF                       (idx, [1:   6]) = [  9.06654E-03 0.00016  7.49484E-03 9.3E-05  1.05729E-01 0.00046 ];
RECIPVEL                  (idx, [1:   6]) = [  6.70716E-09 0.00036  4.49552E-09 0.00016  1.42713E-07 0.00068 ];
FISSE                     (idx, [1:   6]) = [  1.99173E+02 1.6E-07  1.99150E+02 1.7E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 2.5E-07  1.16233E-06 0.21604 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 2.1E-07  8.33634E-07 0.25640 ];
CHID                      (idx, [1:   4]) = [  9.99907E-01 3.8E-05  9.27808E-05 0.40868 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.96167E-01 2.6E-06  0.00000E+00 0.0E+00  3.83338E-03 0.00067  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.78819E-01 3.4E-05  0.00000E+00 0.0E+00  1.07293E-03 0.00067  3.09354E-01 0.00021 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.96270E-01 2.6E-06  0.00000E+00 0.0E+00  3.83338E-03 0.00067  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.78848E-01 3.4E-05  0.00000E+00 0.0E+00  1.07293E-03 0.00067  3.09354E-01 0.00021 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.80363E-01 3.3E-05  2.79891E-01 3.4E-05  3.09354E-01 0.00021 ];
SCATT1                    (idx, [1:   6]) = [  4.53982E-02 0.00015  4.55970E-02 0.00015  3.31715E-02 0.00168 ];
SCATT2                    (idx, [1:   6]) = [  1.87811E-02 0.00030  1.89070E-02 0.00030  1.10348E-02 0.00401 ];
SCATT3                    (idx, [1:   6]) = [  4.03435E-03 0.00117  4.09535E-03 0.00116  2.84018E-04 0.13306 ];
SCATT4                    (idx, [1:   6]) = [  1.33470E-03 0.00328  1.38553E-03 0.00320 -1.79156E-03 0.01865 ];
SCATT5                    (idx, [1:   6]) = [  1.00929E-03 0.00366  1.03086E-03 0.00364 -3.15994E-04 0.09310 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.43217E-01 4.8E-05  2.41607E-01 4.8E-05  3.42246E-01 0.00029 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.37052E+00 4.8E-05  1.37965E+00 4.8E-05  9.74041E-01 0.00029 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.61927E-01 0.00016  1.62910E-01 0.00016  1.07238E-01 0.00171 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.09836E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  5.92419E-04 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  1.16656E-06 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.14010E-01 0.0E+00  2.12733E-01 0.0E+00  3.39257E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.55756E+00 0.0E+00  1.56691E+00 0.0E+00  9.82540E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98268 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '334' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  1.99310E+18 0.00017  1.96219E+18 0.00017  3.09105E+16 0.00072 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  2.88034E-01 3.4E-05  2.86678E-01 3.4E-05  3.74110E-01 0.00020 ];
FISSXS                    (idx, [1:   6]) = [  3.57941E-03 0.00016  2.96906E-03 9.6E-05  4.23259E-02 0.00046 ];
CAPTXS                    (idx, [1:   6]) = [  4.62465E-03 0.00014  4.32764E-03 0.00014  2.34823E-02 0.00082 ];
ABSXS                     (idx, [1:   6]) = [  8.20406E-03 0.00013  7.29671E-03 0.00011  6.58082E-02 0.00046 ];
RABSXS                    (idx, [1:   6]) = [  8.17581E-03 0.00013  7.26802E-03 0.00011  6.58082E-02 0.00046 ];
ELAXS                     (idx, [1:   6]) = [  2.67914E-01 3.6E-05  2.67278E-01 3.7E-05  3.08302E-01 0.00018 ];
INELAXS                   (idx, [1:   6]) = [  1.19164E-02 0.00012  1.21041E-02 0.00012  1.48603E-17 0.00055 ];
SCATTXS                   (idx, [1:   6]) = [  2.79830E-01 3.3E-05  2.79382E-01 3.3E-05  3.08302E-01 0.00018 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.79858E-01 3.3E-05  2.79410E-01 3.3E-05  3.08302E-01 0.00018 ];
REMXS                     (idx, [1:   6]) = [  8.17462E-03 0.00037  8.30249E-03 0.00037  6.58529E-02 0.00069 ];
NUBAR                     (idx, [1:   6]) = [  2.51171E+00 1.6E-05  2.51700E+00 1.9E-05  2.48815E+00 1.7E-07 ];
NSF                       (idx, [1:   6]) = [  8.99042E-03 0.00016  7.47313E-03 9.8E-05  1.05313E-01 0.00046 ];
RECIPVEL                  (idx, [1:   6]) = [  6.60210E-09 0.00036  4.47535E-09 0.00016  1.41606E-07 0.00069 ];
FISSE                     (idx, [1:   6]) = [  1.99173E+02 1.7E-07  1.99150E+02 1.9E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 1.7E-07  4.78911E-07 0.35234 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 1.6E-07  4.20219E-07 0.37686 ];
CHID                      (idx, [1:   4]) = [  9.99983E-01 1.7E-05  1.72414E-05 1.00000 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.96291E-01 2.5E-06  0.00000E+00 0.0E+00  3.70908E-03 0.00068  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.78347E-01 3.6E-05  0.00000E+00 0.0E+00  1.03625E-03 0.00068  3.08257E-01 0.00023 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.96394E-01 2.6E-06  0.00000E+00 0.0E+00  3.70908E-03 0.00068  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.78376E-01 3.6E-05  0.00000E+00 0.0E+00  1.03625E-03 0.00068  3.08257E-01 0.00023 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.79831E-01 3.5E-05  2.79383E-01 3.5E-05  3.08257E-01 0.00023 ];
SCATT1                    (idx, [1:   6]) = [  4.50163E-02 0.00016  4.52155E-02 0.00016  3.23734E-02 0.00189 ];
SCATT2                    (idx, [1:   6]) = [  1.86217E-02 0.00031  1.87456E-02 0.00031  1.07552E-02 0.00426 ];
SCATT3                    (idx, [1:   6]) = [  4.02422E-03 0.00117  4.08208E-03 0.00117  3.50124E-04 0.11347 ];
SCATT4                    (idx, [1:   6]) = [  1.33869E-03 0.00318  1.38912E-03 0.00304 -1.86257E-03 0.01794 ];
SCATT5                    (idx, [1:   6]) = [  9.94323E-04 0.00382  1.01430E-03 0.00379 -2.73925E-04 0.11174 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.43018E-01 5.0E-05  2.41463E-01 5.1E-05  3.41736E-01 0.00030 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.37165E+00 5.0E-05  1.38048E+00 5.1E-05  9.75500E-01 0.00030 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.60870E-01 0.00016  1.61841E-01 0.00016  1.05031E-01 0.00192 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.09559E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  5.71781E-04 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  4.76221E-07 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.13982E-01 0.0E+00  2.12747E-01 0.0E+00  3.38806E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.55776E+00 0.0E+00  1.56680E+00 0.0E+00  9.83846E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98268 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '335' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  1.85403E+18 0.00018  1.82600E+18 0.00018  2.80266E+16 0.00075 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  2.87536E-01 3.5E-05  2.86223E-01 3.6E-05  3.73078E-01 0.00022 ];
FISSXS                    (idx, [1:   6]) = [  3.55453E-03 0.00016  2.96219E-03 0.00010  4.21506E-02 0.00051 ];
CAPTXS                    (idx, [1:   6]) = [  4.61001E-03 0.00015  4.32017E-03 0.00015  2.34982E-02 0.00088 ];
ABSXS                     (idx, [1:   6]) = [  8.16455E-03 0.00014  7.28235E-03 0.00012  6.56488E-02 0.00049 ];
RABSXS                    (idx, [1:   6]) = [  8.13652E-03 0.00014  7.25390E-03 0.00012  6.56488E-02 0.00049 ];
ELAXS                     (idx, [1:   6]) = [  2.67483E-01 3.9E-05  2.66870E-01 3.9E-05  3.07429E-01 0.00019 ];
INELAXS                   (idx, [1:   6]) = [  1.18884E-02 0.00014  1.20709E-02 0.00013  1.48818E-17 0.00058 ];
SCATTXS                   (idx, [1:   6]) = [  2.79371E-01 3.5E-05  2.78941E-01 3.5E-05  3.07429E-01 0.00019 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.79399E-01 3.5E-05  2.78969E-01 3.5E-05  3.07429E-01 0.00019 ];
REMXS                     (idx, [1:   6]) = [  8.13403E-03 0.00038  8.25738E-03 0.00037  6.56433E-02 0.00079 ];
NUBAR                     (idx, [1:   6]) = [  2.51188E+00 1.6E-05  2.51706E+00 2.0E-05  2.48815E+00 1.9E-07 ];
NSF                       (idx, [1:   6]) = [  8.92854E-03 0.00016  7.45599E-03 0.00010  1.04877E-01 0.00051 ];
RECIPVEL                  (idx, [1:   6]) = [  6.51657E-09 0.00037  4.45903E-09 0.00018  1.40568E-07 0.00073 ];
FISSE                     (idx, [1:   6]) = [  1.99172E+02 1.8E-07  1.99150E+02 2.0E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 2.6E-07  1.09762E-06 0.24060 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 1.6E-07  3.89036E-07 0.40724 ];
CHID                      (idx, [1:   4]) = [  9.99800E-01 6.0E-05  1.99546E-04 0.30253 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.96394E-01 2.7E-06  0.00000E+00 0.0E+00  3.60569E-03 0.00076  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.77937E-01 3.8E-05  0.00000E+00 0.0E+00  1.00578E-03 0.00076  3.07434E-01 0.00024 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.96496E-01 2.8E-06  0.00000E+00 0.0E+00  3.60569E-03 0.00076  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.77966E-01 3.8E-05  0.00000E+00 0.0E+00  1.00578E-03 0.00076  3.07434E-01 0.00024 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.79374E-01 3.7E-05  2.78943E-01 3.8E-05  3.07434E-01 0.00024 ];
SCATT1                    (idx, [1:   6]) = [  4.46676E-02 0.00017  4.48634E-02 0.00017  3.19062E-02 0.00193 ];
SCATT2                    (idx, [1:   6]) = [  1.84746E-02 0.00032  1.85961E-02 0.00032  1.05550E-02 0.00468 ];
SCATT3                    (idx, [1:   6]) = [  4.00808E-03 0.00124  4.06474E-03 0.00123  3.15730E-04 0.13000 ];
SCATT4                    (idx, [1:   6]) = [  1.34614E-03 0.00320  1.39308E-03 0.00312 -1.71232E-03 0.02155 ];
SCATT5                    (idx, [1:   6]) = [  9.92592E-04 0.00397  1.01232E-03 0.00395 -2.92859E-04 0.11432 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.42868E-01 5.4E-05  2.41360E-01 5.4E-05  3.41171E-01 0.00033 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.37249E+00 5.4E-05  1.38107E+00 5.4E-05  9.77133E-01 0.00033 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.59885E-01 0.00017  1.60834E-01 0.00017  1.03793E-01 0.00197 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.09304E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  5.53474E-04 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  1.09525E-06 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.13967E-01 0.0E+00  2.12767E-01 0.0E+00  3.38252E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.55787E+00 0.0E+00  1.56666E+00 0.0E+00  9.85459E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98268 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '336' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  1.70189E+18 0.00020  1.67666E+18 0.00020  2.52295E+16 0.00081 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  2.87126E-01 3.6E-05  2.85849E-01 3.7E-05  3.72037E-01 0.00024 ];
FISSXS                    (idx, [1:   6]) = [  3.53495E-03 0.00018  2.95643E-03 0.00011  4.19844E-02 0.00052 ];
CAPTXS                    (idx, [1:   6]) = [  4.59603E-03 0.00016  4.31260E-03 0.00015  2.34373E-02 0.00094 ];
ABSXS                     (idx, [1:   6]) = [  8.13098E-03 0.00015  7.26903E-03 0.00012  6.54216E-02 0.00054 ];
RABSXS                    (idx, [1:   6]) = [  8.10310E-03 0.00015  7.24073E-03 0.00012  6.54216E-02 0.00054 ];
ELAXS                     (idx, [1:   6]) = [  2.67129E-01 3.9E-05  2.66535E-01 4.0E-05  3.06616E-01 0.00021 ];
INELAXS                   (idx, [1:   6]) = [  1.18661E-02 0.00014  1.20447E-02 0.00014  1.49454E-17 0.00060 ];
SCATTXS                   (idx, [1:   6]) = [  2.78995E-01 3.5E-05  2.78580E-01 3.6E-05  3.06616E-01 0.00021 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.79023E-01 3.5E-05  2.78608E-01 3.6E-05  3.06616E-01 0.00021 ];
REMXS                     (idx, [1:   6]) = [  8.09925E-03 0.00042  8.21971E-03 0.00041  6.53942E-02 0.00082 ];
NUBAR                     (idx, [1:   6]) = [  2.51201E+00 1.7E-05  2.51710E+00 2.1E-05  2.48816E+00 1.9E-07 ];
NSF                       (idx, [1:   6]) = [  8.87981E-03 0.00018  7.44162E-03 0.00011  1.04464E-01 0.00052 ];
RECIPVEL                  (idx, [1:   6]) = [  6.45318E-09 0.00039  4.44542E-09 0.00019  1.39876E-07 0.00075 ];
FISSE                     (idx, [1:   6]) = [  1.99172E+02 1.9E-07  1.99151E+02 2.0E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 2.7E-07  1.05412E-06 0.25641 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 2.1E-07  6.32996E-07 0.33202 ];
CHID                      (idx, [1:   4]) = [  9.99882E-01 4.9E-05  1.18239E-04 0.41316 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.96474E-01 2.9E-06  0.00000E+00 0.0E+00  3.52621E-03 0.00081  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.77601E-01 3.9E-05  0.00000E+00 0.0E+00  9.82345E-04 0.00081  3.06643E-01 0.00026 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.96575E-01 2.9E-06  0.00000E+00 0.0E+00  3.52621E-03 0.00081  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.77629E-01 3.9E-05  0.00000E+00 0.0E+00  9.82345E-04 0.00081  3.06643E-01 0.00026 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.78999E-01 3.8E-05  2.78583E-01 3.8E-05  3.06643E-01 0.00026 ];
SCATT1                    (idx, [1:   6]) = [  4.44009E-02 0.00018  4.45983E-02 0.00018  3.12791E-02 0.00212 ];
SCATT2                    (idx, [1:   6]) = [  1.83544E-02 0.00036  1.84752E-02 0.00036  1.03230E-02 0.00501 ];
SCATT3                    (idx, [1:   6]) = [  3.99886E-03 0.00129  4.05492E-03 0.00130  2.72189E-04 0.16430 ];
SCATT4                    (idx, [1:   6]) = [  1.36196E-03 0.00334  1.40831E-03 0.00327 -1.71756E-03 0.02255 ];
SCATT5                    (idx, [1:   6]) = [  9.92813E-04 0.00412  1.01298E-03 0.00409 -3.48080E-04 0.09985 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.42725E-01 5.6E-05  2.41251E-01 5.6E-05  3.40758E-01 0.00036 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.37330E+00 5.6E-05  1.38169E+00 5.6E-05  9.78335E-01 0.00036 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.59144E-01 0.00018  1.60090E-01 0.00018  1.02019E-01 0.00217 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.09225E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  5.46196E-04 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  1.05899E-06 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.13933E-01 0.0E+00  2.12759E-01 0.0E+00  3.37904E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.55812E+00 0.0E+00  1.56672E+00 0.0E+00  9.86475E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98268 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '337' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  1.53733E+18 0.00022  1.51486E+18 0.00022  2.24759E+16 0.00084 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  2.86799E-01 4.1E-05  2.85547E-01 4.2E-05  3.71240E-01 0.00026 ];
FISSXS                    (idx, [1:   6]) = [  3.52233E-03 0.00018  2.95360E-03 0.00011  4.18585E-02 0.00057 ];
CAPTXS                    (idx, [1:   6]) = [  4.58945E-03 0.00017  4.31017E-03 0.00016  2.34175E-02 0.00100 ];
ABSXS                     (idx, [1:   6]) = [  8.11178E-03 0.00015  7.26377E-03 0.00013  6.52760E-02 0.00057 ];
RABSXS                    (idx, [1:   6]) = [  8.08389E-03 0.00015  7.23546E-03 0.00013  6.52760E-02 0.00057 ];
ELAXS                     (idx, [1:   6]) = [  2.66845E-01 4.4E-05  2.66264E-01 4.5E-05  3.05964E-01 0.00023 ];
INELAXS                   (idx, [1:   6]) = [  1.18431E-02 0.00015  1.20188E-02 0.00015  1.49047E-17 0.00067 ];
SCATTXS                   (idx, [1:   6]) = [  2.78688E-01 4.0E-05  2.78283E-01 4.1E-05  3.05964E-01 0.00023 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.78715E-01 4.0E-05  2.78311E-01 4.1E-05  3.05964E-01 0.00023 ];
REMXS                     (idx, [1:   6]) = [  8.08074E-03 0.00043  8.19491E-03 0.00043  6.52914E-02 0.00087 ];
NUBAR                     (idx, [1:   6]) = [  2.51190E+00 1.8E-05  2.51689E+00 2.2E-05  2.48816E+00 2.1E-07 ];
NSF                       (idx, [1:   6]) = [  8.84773E-03 0.00018  7.43388E-03 0.00012  1.04151E-01 0.00057 ];
RECIPVEL                  (idx, [1:   6]) = [  6.41015E-09 0.00041  4.43879E-09 0.00020  1.39272E-07 0.00082 ];
FISSE                     (idx, [1:   6]) = [  1.99172E+02 2.0E-07  1.99151E+02 2.2E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 2.6E-07  8.62333E-07 0.30005 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 2.3E-07  7.07441E-07 0.33205 ];
CHID                      (idx, [1:   4]) = [  9.99955E-01 3.2E-05  4.54082E-05 0.71036 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.96541E-01 2.9E-06  0.00000E+00 0.0E+00  3.45938E-03 0.00083  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.77324E-01 4.4E-05  0.00000E+00 0.0E+00  9.62695E-04 0.00083  3.05949E-01 0.00028 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.96642E-01 2.9E-06  0.00000E+00 0.0E+00  3.45938E-03 0.00083  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.77352E-01 4.4E-05  0.00000E+00 0.0E+00  9.62695E-04 0.00083  3.05949E-01 0.00028 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.78691E-01 4.3E-05  2.78287E-01 4.3E-05  3.05949E-01 0.00028 ];
SCATT1                    (idx, [1:   6]) = [  4.41459E-02 0.00018  4.43424E-02 0.00018  3.08991E-02 0.00222 ];
SCATT2                    (idx, [1:   6]) = [  1.82509E-02 0.00036  1.83708E-02 0.00036  1.01686E-02 0.00527 ];
SCATT3                    (idx, [1:   6]) = [  3.97864E-03 0.00138  4.03309E-03 0.00138  3.08901E-04 0.14513 ];
SCATT4                    (idx, [1:   6]) = [  1.35982E-03 0.00363  1.40623E-03 0.00354 -1.76704E-03 0.02391 ];
SCATT5                    (idx, [1:   6]) = [  9.92567E-04 0.00451  1.01092E-03 0.00446 -2.45451E-04 0.14659 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.42653E-01 6.1E-05  2.41205E-01 6.2E-05  3.40341E-01 0.00038 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.37371E+00 6.1E-05  1.38196E+00 6.2E-05  9.79548E-01 0.00038 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.58405E-01 0.00019  1.59341E-01 0.00019  1.01007E-01 0.00226 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.09067E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  5.35428E-04 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  8.62438E-07 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.13918E-01 0.0E+00  2.12762E-01 0.0E+00  3.37489E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.55823E+00 0.0E+00  1.56670E+00 0.0E+00  9.87685E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98268 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '338' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  1.36209E+18 0.00024  1.34225E+18 0.00024  1.98388E+16 0.00087 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  2.86584E-01 4.0E-05  2.85342E-01 4.1E-05  3.70631E-01 0.00027 ];
FISSXS                    (idx, [1:   6]) = [  3.52054E-03 0.00019  2.95403E-03 0.00012  4.18531E-02 0.00059 ];
CAPTXS                    (idx, [1:   6]) = [  4.59098E-03 0.00018  4.31285E-03 0.00017  2.34148E-02 0.00106 ];
ABSXS                     (idx, [1:   6]) = [  8.11153E-03 0.00016  7.26689E-03 0.00013  6.52679E-02 0.00060 ];
RABSXS                    (idx, [1:   6]) = [  8.08375E-03 0.00016  7.23870E-03 0.00013  6.52679E-02 0.00060 ];
ELAXS                     (idx, [1:   6]) = [  2.66651E-01 4.3E-05  2.66079E-01 4.4E-05  3.05363E-01 0.00024 ];
INELAXS                   (idx, [1:   6]) = [  1.18212E-02 0.00016  1.19959E-02 0.00015  1.46643E-17 0.00070 ];
SCATTXS                   (idx, [1:   6]) = [  2.78472E-01 3.9E-05  2.78075E-01 4.0E-05  3.05363E-01 0.00024 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.78500E-01 3.9E-05  2.78103E-01 4.0E-05  3.05363E-01 0.00024 ];
REMXS                     (idx, [1:   6]) = [  8.08483E-03 0.00045  8.19256E-03 0.00045  6.52163E-02 0.00090 ];
NUBAR                     (idx, [1:   6]) = [  2.51204E+00 1.8E-05  2.51704E+00 2.2E-05  2.48816E+00 2.1E-07 ];
NSF                       (idx, [1:   6]) = [  8.84373E-03 0.00019  7.43541E-03 0.00012  1.04137E-01 0.00059 ];
RECIPVEL                  (idx, [1:   6]) = [  6.40546E-09 0.00043  4.44187E-09 0.00020  1.39252E-07 0.00086 ];
FISSE                     (idx, [1:   6]) = [  1.99173E+02 2.0E-07  1.99151E+02 2.2E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 2.8E-07  8.89391E-07 0.31483 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 2.3E-07  6.22587E-07 0.37684 ];
CHID                      (idx, [1:   4]) = [  9.99916E-01 5.0E-05  8.38936E-05 0.59261 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.96577E-01 3.1E-06  0.00000E+00 0.0E+00  3.42300E-03 0.00090  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.77121E-01 4.3E-05  0.00000E+00 0.0E+00  9.51843E-04 0.00090  3.05415E-01 0.00030 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.96678E-01 3.2E-06  0.00000E+00 0.0E+00  3.42300E-03 0.00090  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.77150E-01 4.3E-05  0.00000E+00 0.0E+00  9.51843E-04 0.00090  3.05415E-01 0.00030 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.78471E-01 4.3E-05  2.78073E-01 4.3E-05  3.05415E-01 0.00030 ];
SCATT1                    (idx, [1:   6]) = [  4.39275E-02 0.00020  4.41259E-02 0.00020  3.05023E-02 0.00245 ];
SCATT2                    (idx, [1:   6]) = [  1.81674E-02 0.00039  1.82882E-02 0.00039  9.99629E-03 0.00578 ];
SCATT3                    (idx, [1:   6]) = [  3.96919E-03 0.00145  4.02401E-03 0.00144  2.58873E-04 0.18364 ];
SCATT4                    (idx, [1:   6]) = [  1.37318E-03 0.00360  1.41799E-03 0.00351 -1.65795E-03 0.02584 ];
SCATT5                    (idx, [1:   6]) = [  9.88579E-04 0.00465  1.00829E-03 0.00459 -3.46768E-04 0.11438 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.42656E-01 6.0E-05  2.41216E-01 6.1E-05  3.40129E-01 0.00040 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.37369E+00 6.0E-05  1.38189E+00 6.2E-05  9.80177E-01 0.00040 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.57745E-01 0.00021  1.58685E-01 0.00021  9.98892E-02 0.00250 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.08938E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  5.27839E-04 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  8.85890E-07 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.13999E-01 0.0E+00  2.12849E-01 0.0E+00  3.37278E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.55764E+00 0.0E+00  1.56606E+00 0.0E+00  9.88305E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98267 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '339' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  1.17847E+18 0.00026  1.16089E+18 0.00026  1.75778E+16 0.00096 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  2.86548E-01 4.5E-05  2.85283E-01 4.6E-05  3.70091E-01 0.00029 ];
FISSXS                    (idx, [1:   6]) = [  3.54499E-03 0.00021  2.96286E-03 0.00013  4.19939E-02 0.00062 ];
CAPTXS                    (idx, [1:   6]) = [  4.61405E-03 0.00020  4.33166E-03 0.00019  2.32695E-02 0.00111 ];
ABSXS                     (idx, [1:   6]) = [  8.15904E-03 0.00017  7.29453E-03 0.00015  6.52634E-02 0.00062 ];
RABSXS                    (idx, [1:   6]) = [  8.13143E-03 0.00017  7.26650E-03 0.00015  6.52634E-02 0.00062 ];
ELAXS                     (idx, [1:   6]) = [  2.66616E-01 4.9E-05  2.66037E-01 4.9E-05  3.04827E-01 0.00026 ];
INELAXS                   (idx, [1:   6]) = [  1.17730E-02 0.00017  1.19512E-02 0.00017  1.46933E-17 0.00074 ];
SCATTXS                   (idx, [1:   6]) = [  2.78389E-01 4.4E-05  2.77989E-01 4.5E-05  3.04827E-01 0.00026 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.78416E-01 4.4E-05  2.78017E-01 4.5E-05  3.04827E-01 0.00026 ];
REMXS                     (idx, [1:   6]) = [  8.13461E-03 0.00046  8.22291E-03 0.00046  6.53745E-02 0.00100 ];
NUBAR                     (idx, [1:   6]) = [  2.51171E+00 2.0E-05  2.51677E+00 2.5E-05  2.48815E+00 2.4E-07 ];
NSF                       (idx, [1:   6]) = [  8.90399E-03 0.00021  7.45685E-03 0.00013  1.04487E-01 0.00062 ];
RECIPVEL                  (idx, [1:   6]) = [  6.50320E-09 0.00048  4.47022E-09 0.00023  1.40756E-07 0.00091 ];
FISSE                     (idx, [1:   6]) = [  1.99174E+02 2.2E-07  1.99152E+02 2.4E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 3.6E-07  1.11255E-06 0.32794 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 2.8E-07  8.05157E-07 0.35233 ];
CHID                      (idx, [1:   4]) = [  9.99919E-01 6.0E-05  8.12030E-05 0.73718 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.96566E-01 3.2E-06  0.00000E+00 0.0E+00  3.43399E-03 0.00092  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.77032E-01 4.8E-05  0.00000E+00 0.0E+00  9.54603E-04 0.00092  3.04716E-01 0.00032 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.96667E-01 3.2E-06  0.00000E+00 0.0E+00  3.43399E-03 0.00092  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.77060E-01 4.8E-05  0.00000E+00 0.0E+00  9.54603E-04 0.00092  3.04716E-01 0.00032 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.78385E-01 4.8E-05  2.77987E-01 4.8E-05  3.04716E-01 0.00032 ];
SCATT1                    (idx, [1:   6]) = [  4.37339E-02 0.00022  4.39394E-02 0.00022  3.01583E-02 0.00262 ];
SCATT2                    (idx, [1:   6]) = [  1.80773E-02 0.00040  1.82004E-02 0.00040  9.95027E-03 0.00597 ];
SCATT3                    (idx, [1:   6]) = [  3.96658E-03 0.00161  4.02245E-03 0.00160  2.73086E-04 0.19813 ];
SCATT4                    (idx, [1:   6]) = [  1.36445E-03 0.00407  1.41025E-03 0.00397 -1.65972E-03 0.02710 ];
SCATT5                    (idx, [1:   6]) = [  9.79711E-04 0.00502  9.99460E-04 0.00496 -3.24738E-04 0.12615 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.42814E-01 7.0E-05  2.41344E-01 7.1E-05  3.39932E-01 0.00043 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.37280E+00 7.0E-05  1.38116E+00 7.1E-05  9.80766E-01 0.00043 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.57099E-01 0.00023  1.58063E-01 0.00023  9.89900E-02 0.00267 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.09223E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  5.48176E-04 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  1.11648E-06 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.14176E-01 0.0E+00  2.13000E-01 0.0E+00  3.37056E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.55635E+00 0.0E+00  1.56494E+00 0.0E+00  9.88955E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98267 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '340' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  9.88988E+17 0.00029  9.72768E+17 0.00029  1.62197E+16 0.00105 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  2.87072E-01 5.0E-05  2.85676E-01 5.0E-05  3.70848E-01 0.00028 ];
FISSXS                    (idx, [1:   6]) = [  3.65058E-03 0.00024  2.99132E-03 0.00014  4.31956E-02 0.00068 ];
CAPTXS                    (idx, [1:   6]) = [  4.69708E-03 0.00021  4.38960E-03 0.00021  2.31446E-02 0.00116 ];
ABSXS                     (idx, [1:   6]) = [  8.34766E-03 0.00020  7.38091E-03 0.00017  6.63402E-02 0.00068 ];
RABSXS                    (idx, [1:   6]) = [  8.32025E-03 0.00020  7.35305E-03 0.00017  6.63402E-02 0.00068 ];
ELAXS                     (idx, [1:   6]) = [  2.67088E-01 5.4E-05  2.66464E-01 5.5E-05  3.04508E-01 0.00024 ];
INELAXS                   (idx, [1:   6]) = [  1.16370E-02 0.00019  1.18311E-02 0.00019  1.47419E-17 0.00078 ];
SCATTXS                   (idx, [1:   6]) = [  2.78725E-01 4.9E-05  2.78295E-01 4.9E-05  3.04508E-01 0.00024 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.78752E-01 4.9E-05  2.78323E-01 4.9E-05  3.04508E-01 0.00024 ];
REMXS                     (idx, [1:   6]) = [  8.32686E-03 0.00050  8.34501E-03 0.00050  6.63889E-02 0.00100 ];
NUBAR                     (idx, [1:   6]) = [  2.51088E+00 2.1E-05  2.51636E+00 2.5E-05  2.48813E+00 2.3E-07 ];
NSF                       (idx, [1:   6]) = [  9.16616E-03 0.00024  7.52723E-03 0.00014  1.07476E-01 0.00068 ];
RECIPVEL                  (idx, [1:   6]) = [  6.93793E-09 0.00055  4.56316E-09 0.00025  1.49356E-07 0.00099 ];
FISSE                     (idx, [1:   6]) = [  1.99178E+02 2.4E-07  1.99154E+02 2.7E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 3.7E-07  1.16835E-06 0.31483 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 3.1E-07  8.22598E-07 0.37688 ];
CHID                      (idx, [1:   4]) = [  9.99893E-01 6.4E-05  1.06891E-04 0.60098 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.96458E-01 3.7E-06  0.00000E+00 0.0E+00  3.54227E-03 0.00105  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.77304E-01 5.3E-05  0.00000E+00 0.0E+00  9.85776E-04 0.00105  3.04459E-01 0.00031 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.96556E-01 3.8E-06  0.00000E+00 0.0E+00  3.54227E-03 0.00105  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.77331E-01 5.3E-05  0.00000E+00 0.0E+00  9.85776E-04 0.00105  3.04459E-01 0.00031 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.78718E-01 5.2E-05  2.78289E-01 5.3E-05  3.04459E-01 0.00031 ];
SCATT1                    (idx, [1:   6]) = [  4.34340E-02 0.00023  4.36594E-02 0.00023  2.99192E-02 0.00265 ];
SCATT2                    (idx, [1:   6]) = [  1.79201E-02 0.00044  1.80534E-02 0.00044  9.92309E-03 0.00646 ];
SCATT3                    (idx, [1:   6]) = [  3.91550E-03 0.00175  3.97519E-03 0.00174  3.35134E-04 0.16136 ];
SCATT4                    (idx, [1:   6]) = [  1.34369E-03 0.00449  1.39311E-03 0.00435 -1.62033E-03 0.02872 ];
SCATT5                    (idx, [1:   6]) = [  9.74888E-04 0.00542  9.97216E-04 0.00536 -3.63294E-04 0.11909 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.43638E-01 7.4E-05  2.42017E-01 7.5E-05  3.40929E-01 0.00041 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.36816E+00 7.4E-05  1.37732E+00 7.5E-05  9.77884E-01 0.00041 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.55835E-01 0.00024  1.56885E-01 0.00024  9.82860E-02 0.00269 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.09804E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  5.98250E-04 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  1.17814E-06 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.14967E-01 0.0E+00  2.13671E-01 0.0E+00  3.37850E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.55063E+00 0.0E+00  1.56003E+00 0.0E+00  9.86632E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98267 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '341' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  7.96666E+17 0.00032  7.78490E+17 0.00032  1.81767E+16 0.00098 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  2.89821E-01 5.2E-05  2.87721E-01 5.3E-05  3.79777E-01 0.00029 ];
FISSXS                    (idx, [1:   6]) = [  4.19022E-03 0.00028  3.07797E-03 0.00016  5.18378E-02 0.00067 ];
CAPTXS                    (idx, [1:   6]) = [  5.01476E-03 0.00023  4.57720E-03 0.00021  2.37621E-02 0.00108 ];
ABSXS                     (idx, [1:   6]) = [  9.20498E-03 0.00021  7.65516E-03 0.00018  7.55998E-02 0.00066 ];
RABSXS                    (idx, [1:   6]) = [  9.17895E-03 0.00022  7.62852E-03 0.00018  7.55998E-02 0.00066 ];
ELAXS                     (idx, [1:   6]) = [  2.69504E-01 5.7E-05  2.68695E-01 5.8E-05  3.04177E-01 0.00025 ];
INELAXS                   (idx, [1:   6]) = [  1.11119E-02 0.00022  1.13714E-02 0.00022  1.49913E-17 0.00072 ];
SCATTXS                   (idx, [1:   6]) = [  2.80616E-01 5.1E-05  2.80066E-01 5.2E-05  3.04177E-01 0.00025 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.80642E-01 5.1E-05  2.80093E-01 5.2E-05  3.04177E-01 0.00025 ];
REMXS                     (idx, [1:   6]) = [  9.18366E-03 0.00051  8.73141E-03 0.00055  7.55555E-02 0.00089 ];
NUBAR                     (idx, [1:   6]) = [  2.50712E+00 2.1E-05  2.51463E+00 2.9E-05  2.48802E+00 1.9E-07 ];
NSF                       (idx, [1:   6]) = [  1.05054E-02 0.00028  7.73994E-03 0.00016  1.28974E-01 0.00067 ];
RECIPVEL                  (idx, [1:   6]) = [  9.34478E-09 0.00072  4.84670E-09 0.00027  2.02001E-07 0.00110 ];
FISSE                     (idx, [1:   6]) = [  1.99195E+02 2.2E-07  1.99164E+02 2.8E-07  1.99273E+02 7.4E-09 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99999E-01 3.6E-07  7.61685E-07 0.47026 ];
CHIP                      (idx, [1:   4]) = [  9.99999E-01 3.4E-07  6.36085E-07 0.52811 ];
CHID                      (idx, [1:   4]) = [  9.99970E-01 3.0E-05  3.03030E-05 1.00000 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.96084E-01 4.1E-06  0.00000E+00 0.0E+00  3.91602E-03 0.00105  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.78963E-01 5.6E-05  0.00000E+00 0.0E+00  1.09672E-03 0.00105  3.04222E-01 0.00032 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.96179E-01 4.2E-06  0.00000E+00 0.0E+00  3.91602E-03 0.00105  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.78990E-01 5.6E-05  0.00000E+00 0.0E+00  1.09672E-03 0.00105  3.04222E-01 0.00032 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.80611E-01 5.5E-05  2.80060E-01 5.6E-05  3.04222E-01 0.00032 ];
SCATT1                    (idx, [1:   6]) = [  4.27767E-02 0.00028  4.30849E-02 0.00028  2.95729E-02 0.00254 ];
SCATT2                    (idx, [1:   6]) = [  1.74858E-02 0.00053  1.76715E-02 0.00053  9.53337E-03 0.00619 ];
SCATT3                    (idx, [1:   6]) = [  3.68889E-03 0.00205  3.76601E-03 0.00203  3.84828E-04 0.13635 ];
SCATT4                    (idx, [1:   6]) = [  1.19674E-03 0.00560  1.26294E-03 0.00538 -1.63779E-03 0.02694 ];
SCATT5                    (idx, [1:   6]) = [  9.07823E-04 0.00664  9.35868E-04 0.00656 -2.92440E-04 0.13427 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.47044E-01 8.0E-05  2.44637E-01 8.2E-05  3.50204E-01 0.00041 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.34929E+00 8.0E-05  1.36257E+00 8.2E-05  9.51986E-01 0.00041 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.52442E-01 0.00029  1.53842E-01 0.00029  9.72247E-02 0.00258 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.14114E+00 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [  9.62960E-04 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99999E-01 0.0E+00  7.66043E-07 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.18379E-01 0.0E+00  2.16526E-01 0.0E+00  3.44594E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.52640E+00 0.0E+00  1.53946E+00 0.0E+00  9.67322E-01 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98267 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '342' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  6.01760E+17 0.00035  5.72904E+17 0.00035  2.88561E+16 0.00105 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  2.95294E-01 5.9E-05  2.94034E-01 6.1E-05  3.20318E-01 0.00020 ];
FISSXS                    (idx, [1:   6]) = [  9.80282E-05 0.00068  1.02966E-04 0.00068  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  5.51033E-03 0.00027  5.04350E-03 0.00025  1.47828E-02 0.00117 ];
ABSXS                     (idx, [1:   6]) = [  5.60836E-03 0.00026  5.14647E-03 0.00024  1.47828E-02 0.00117 ];
RABSXS                    (idx, [1:   6]) = [  5.59082E-03 0.00026  5.12804E-03 0.00024  1.47828E-02 0.00117 ];
ELAXS                     (idx, [1:   6]) = [  2.80316E-01 6.3E-05  2.79046E-01 6.6E-05  3.05536E-01 0.00019 ];
INELAXS                   (idx, [1:   6]) = [  9.37002E-03 0.00027  9.84195E-03 0.00027  1.22169E-17 0.00063 ];
SCATTXS                   (idx, [1:   6]) = [  2.89686E-01 5.8E-05  2.88888E-01 6.0E-05  3.05536E-01 0.00019 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.89703E-01 5.8E-05  2.88906E-01 6.0E-05  3.05536E-01 0.00019 ];
REMXS                     (idx, [1:   6]) = [  5.58604E-03 0.00098  6.55904E-03 0.00085  1.47556E-02 0.00204 ];
NUBAR                     (idx, [1:   6]) = [  2.36250E+00 0.00043  2.36250E+00 0.00043  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  2.31593E-04 0.00082  2.43257E-04 0.00081  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  2.13857E-08 0.00126  5.68347E-09 0.00030  3.33077E-07 0.00124 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99993E-01 7.3E-06  7.29927E-06 1.00000 ];
CHIP                      (idx, [1:   4]) = [  9.99993E-01 7.5E-06  7.46269E-06 1.00000 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.95034E-01 5.6E-06  0.00000E+00 0.0E+00  4.96561E-03 0.00112  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.87457E-01 6.5E-05  0.00000E+00 0.0E+00  1.43451E-03 0.00111  3.05563E-01 0.00021 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.95098E-01 5.6E-06  0.00000E+00 0.0E+00  4.96561E-03 0.00112  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.87475E-01 6.5E-05  0.00000E+00 0.0E+00  1.43451E-03 0.00111  3.05563E-01 0.00021 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.89691E-01 6.2E-05  2.88891E-01 6.4E-05  3.05563E-01 0.00021 ];
SCATT1                    (idx, [1:   6]) = [  4.10226E-02 0.00033  4.16516E-02 0.00034  2.85310E-02 0.00220 ];
SCATT2                    (idx, [1:   6]) = [  1.58736E-02 0.00067  1.62101E-02 0.00066  9.19014E-03 0.00513 ];
SCATT3                    (idx, [1:   6]) = [  2.75470E-03 0.00325  2.86094E-03 0.00322  6.43413E-04 0.06319 ];
SCATT4                    (idx, [1:   6]) = [  4.98991E-04 0.01549  5.90013E-04 0.01330 -1.30810E-03 0.02759 ];
SCATT5                    (idx, [1:   6]) = [  5.93853E-04 0.01170  6.38562E-04 0.01122 -2.94993E-04 0.10936 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.54272E-01 9.1E-05  2.52383E-01 9.5E-05  2.91787E-01 0.00033 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.31095E+00 9.1E-05  1.32076E+00 9.5E-05  1.14251E+00 0.00033 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.41609E-01 0.00034  1.44178E-01 0.00035  9.33796E-02 0.00223 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  4.11915E-02 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -4.10193E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99992E-01 0.0E+00  7.65111E-06 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.29463E-01 0.0E+00  2.27069E-01 0.0E+00  2.90196E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.45267E+00 0.0E+00  1.46798E+00 0.0E+00  1.14865E+00 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98267 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '343' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  4.43610E+17 0.00040  4.10648E+17 0.00040  3.29617E+16 0.00107 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  3.01403E-01 6.9E-05  2.99822E-01 7.3E-05  3.21109E-01 0.00019 ];
FISSXS                    (idx, [1:   6]) = [  7.14439E-05 0.00092  7.71780E-05 0.00091  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  6.18058E-03 0.00032  5.49669E-03 0.00029  1.47042E-02 0.00106 ];
ABSXS                     (idx, [1:   6]) = [  6.25203E-03 0.00032  5.57387E-03 0.00028  1.47042E-02 0.00106 ];
RABSXS                    (idx, [1:   6]) = [  6.23941E-03 0.00032  5.56024E-03 0.00028  1.47042E-02 0.00106 ];
ELAXS                     (idx, [1:   6]) = [  2.87329E-01 7.3E-05  2.85798E-01 7.7E-05  3.06405E-01 0.00018 ];
INELAXS                   (idx, [1:   6]) = [  7.82196E-03 0.00034  8.44977E-03 0.00032  1.21841E-17 0.00061 ];
SCATTXS                   (idx, [1:   6]) = [  2.95151E-01 6.8E-05  2.94248E-01 7.2E-05  3.06405E-01 0.00018 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.95163E-01 6.8E-05  2.94262E-01 7.2E-05  3.06405E-01 0.00018 ];
REMXS                     (idx, [1:   6]) = [  6.23077E-03 0.00100  7.31204E-03 0.00089  1.46809E-02 0.00180 ];
NUBAR                     (idx, [1:   6]) = [  2.36099E+00 0.00059  2.36099E+00 0.00059  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  1.68690E-04 0.00116  1.82229E-04 0.00115  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  3.55936E-08 0.00132  6.45213E-09 0.00035  3.98594E-07 0.00112 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.94022E-01 7.2E-06  0.00000E+00 0.0E+00  5.97798E-03 0.00120  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.92496E-01 7.6E-05  0.00000E+00 0.0E+00  1.75904E-03 0.00120  3.06428E-01 0.00020 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.94068E-01 7.3E-06  0.00000E+00 0.0E+00  5.97798E-03 0.00120  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.92510E-01 7.6E-05  0.00000E+00 0.0E+00  1.75904E-03 0.00120  3.06428E-01 0.00020 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.95159E-01 7.1E-05  2.94255E-01 7.5E-05  3.06428E-01 0.00020 ];
SCATT1                    (idx, [1:   6]) = [  3.95598E-02 0.00041  4.04626E-02 0.00042  2.83119E-02 0.00196 ];
SCATT2                    (idx, [1:   6]) = [  1.47600E-02 0.00081  1.52111E-02 0.00082  9.13687E-03 0.00486 ];
SCATT3                    (idx, [1:   6]) = [  2.17769E-03 0.00494  2.28623E-03 0.00497  8.24853E-04 0.04413 ];
SCATT4                    (idx, [1:   6]) = [  7.51437E-05 0.12224  1.74696E-04 0.05425 -1.16679E-03 0.02915 ];
SCATT5                    (idx, [1:   6]) = [  4.24114E-04 0.01989  4.80640E-04 0.01831 -2.80990E-04 0.10239 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.61843E-01 0.00011  2.59359E-01 0.00011  2.92797E-01 0.00031 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.27304E+00 0.00011  1.28523E+00 0.00011  1.13855E+00 0.00031 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.34030E-01 0.00042  1.37509E-01 0.00043  9.24014E-02 0.00199 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  2.70315E-02 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -4.77847E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.39844E-01 0.0E+00  2.36502E-01 0.0E+00  2.91095E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.38979E+00 0.0E+00  1.40943E+00 0.0E+00  1.14510E+00 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98267 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '344' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  3.21028E+17 0.00045  2.89202E+17 0.00045  3.18258E+16 0.00108 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  3.05610E-01 8.0E-05  3.03847E-01 8.6E-05  3.21642E-01 0.00020 ];
FISSXS                    (idx, [1:   6]) = [  5.67013E-05 0.00125  6.29411E-05 0.00125  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  6.73820E-03 0.00037  5.86562E-03 0.00034  1.46714E-02 0.00108 ];
ABSXS                     (idx, [1:   6]) = [  6.79490E-03 0.00036  5.92857E-03 0.00034  1.46714E-02 0.00108 ];
RABSXS                    (idx, [1:   6]) = [  6.78497E-03 0.00036  5.91754E-03 0.00034  1.46714E-02 0.00108 ];
ELAXS                     (idx, [1:   6]) = [  2.92042E-01 8.3E-05  2.90400E-01 9.0E-05  3.06970E-01 0.00018 ];
INELAXS                   (idx, [1:   6]) = [  6.77334E-03 0.00045  7.51868E-03 0.00043  1.19997E-17 0.00062 ];
SCATTXS                   (idx, [1:   6]) = [  2.98815E-01 7.8E-05  2.97919E-01 8.4E-05  3.06970E-01 0.00018 ];
SCATTPRODXS               (idx, [1:   6]) = [  2.98825E-01 7.8E-05  2.97930E-01 8.4E-05  3.06970E-01 0.00018 ];
REMXS                     (idx, [1:   6]) = [  6.77941E-03 0.00109  7.96474E-03 0.00097  1.46304E-02 0.00195 ];
NUBAR                     (idx, [1:   6]) = [  2.36168E+00 0.00078  2.36168E+00 0.00078  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  1.33919E-04 0.00152  1.48656E-04 0.00151  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  5.02579E-08 0.00138  7.10007E-09 0.00039  4.42369E-07 0.00111 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.93124E-01 8.9E-06  0.00000E+00 0.0E+00  6.87564E-03 0.00129  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.95872E-01 9.1E-05  0.00000E+00 0.0E+00  2.04838E-03 0.00129  3.07011E-01 0.00020 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.93160E-01 9.0E-06  0.00000E+00 0.0E+00  6.87564E-03 0.00129  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.95883E-01 9.1E-05  0.00000E+00 0.0E+00  2.04838E-03 0.00129  3.07011E-01 0.00020 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  2.98821E-01 8.4E-05  2.97920E-01 9.0E-05  3.07011E-01 0.00020 ];
SCATT1                    (idx, [1:   6]) = [  3.84367E-02 0.00049  3.95659E-02 0.00050  2.81738E-02 0.00202 ];
SCATT2                    (idx, [1:   6]) = [  1.40119E-02 0.00105  1.45637E-02 0.00107  8.99665E-03 0.00507 ];
SCATT3                    (idx, [1:   6]) = [  1.84646E-03 0.00654  1.96387E-03 0.00651  7.75150E-04 0.05012 ];
SCATT4                    (idx, [1:   6]) = [ -1.82445E-04 0.05930 -6.73779E-05 0.17002 -1.22800E-03 0.02732 ];
SCATT5                    (idx, [1:   6]) = [  3.06102E-04 0.03148  3.71735E-04 0.02740 -2.89998E-04 0.10547 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.67173E-01 0.00012  2.64282E-01 0.00013  2.93468E-01 0.00031 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.24765E+00 0.00012  1.26130E+00 0.00013  1.13595E+00 0.00031 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.28629E-01 0.00050  1.32808E-01 0.00051  9.17759E-02 0.00205 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.96314E-02 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -5.33939E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.47238E-01 0.0E+00  2.43163E-01 0.0E+00  2.91653E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.34823E+00 0.0E+00  1.37082E+00 0.0E+00  1.14291E+00 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98267 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '345' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  2.28111E+17 0.00051  1.99994E+17 0.00053  2.81176E+16 0.00115 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  3.08803E-01 8.9E-05  3.06916E-01 9.9E-05  3.22233E-01 0.00021 ];
FISSXS                    (idx, [1:   6]) = [  4.70864E-05 0.00163  5.37065E-05 0.00162  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  7.24270E-03 0.00041  6.18775E-03 0.00038  1.47497E-02 0.00114 ];
ABSXS                     (idx, [1:   6]) = [  7.28978E-03 0.00040  6.24146E-03 0.00038  1.47497E-02 0.00114 ];
RABSXS                    (idx, [1:   6]) = [  7.28138E-03 0.00040  6.23188E-03 0.00038  1.47497E-02 0.00114 ];
ELAXS                     (idx, [1:   6]) = [  2.95539E-01 9.1E-05  2.93861E-01 0.00010  3.07483E-01 0.00019 ];
INELAXS                   (idx, [1:   6]) = [  5.97394E-03 0.00057  6.81381E-03 0.00055  1.19921E-17 0.00068 ];
SCATTXS                   (idx, [1:   6]) = [  3.01513E-01 8.7E-05  3.00675E-01 9.7E-05  3.07483E-01 0.00019 ];
SCATTPRODXS               (idx, [1:   6]) = [  3.01521E-01 8.7E-05  3.00684E-01 9.7E-05  3.07483E-01 0.00019 ];
REMXS                     (idx, [1:   6]) = [  7.28159E-03 0.00125  8.53894E-03 0.00113  1.47540E-02 0.00197 ];
NUBAR                     (idx, [1:   6]) = [  2.36200E+00 0.00101  2.36200E+00 0.00101  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  1.11222E-04 0.00193  1.26860E-04 0.00193  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  6.56707E-08 0.00144  7.67184E-09 0.00046  4.78133E-07 0.00112 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  9.99977E-01 2.3E-05  2.27273E-05 1.00000 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  9.98663E-01 0.00134  1.33690E-03 1.00000 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.92327E-01 1.1E-05  0.00000E+00 0.0E+00  7.67287E-03 0.00146  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  2.98367E-01 0.00011  0.00000E+00 0.0E+00  2.30700E-03 0.00146  3.07479E-01 0.00021 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.92360E-01 1.1E-05  0.00000E+00 0.0E+00  7.67287E-03 0.00146  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  2.98377E-01 0.00011  0.00000E+00 0.0E+00  2.30700E-03 0.00146  3.07479E-01 0.00021 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  3.01512E-01 9.4E-05  3.00674E-01 0.00010  3.07479E-01 0.00021 ];
SCATT1                    (idx, [1:   6]) = [  3.74446E-02 0.00060  3.87522E-02 0.00062  2.81425E-02 0.00219 ];
SCATT2                    (idx, [1:   6]) = [  1.34346E-02 0.00129  1.40726E-02 0.00132  8.89868E-03 0.00544 ];
SCATT3                    (idx, [1:   6]) = [  1.59452E-03 0.00898  1.68346E-03 0.00932  9.62188E-04 0.04309 ];
SCATT4                    (idx, [1:   6]) = [ -3.64660E-04 0.03517 -2.59684E-04 0.05311 -1.10992E-03 0.03214 ];
SCATT5                    (idx, [1:   6]) = [  2.33780E-04 0.04863  3.20625E-04 0.03874 -3.85396E-04 0.08578 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.71358E-01 0.00013  2.68164E-01 0.00015  2.94091E-01 0.00033 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.22841E+00 0.00013  1.24305E+00 0.00015  1.13356E+00 0.00033 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.24190E-01 0.00060  1.28886E-01 0.00064  9.15334E-02 0.00222 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.53526E-02 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -5.84334E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  9.99958E-01 0.0E+00  4.18445E-05 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.53100E-01 0.0E+00  2.48429E-01 0.0E+00  2.92178E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.31700E+00 0.0E+00  1.34177E+00 0.0E+00  1.14086E+00 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98267 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '346' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  1.59469E+17 0.00060  1.36090E+17 0.00062  2.33794E+16 0.00126 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  3.11345E-01 0.00010  3.09399E-01 0.00012  3.22679E-01 0.00023 ];
FISSXS                    (idx, [1:   6]) = [  4.00634E-05 0.00201  4.69459E-05 0.00201  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  7.69541E-03 0.00049  6.47307E-03 0.00047  1.48137E-02 0.00123 ];
ABSXS                     (idx, [1:   6]) = [  7.73547E-03 0.00049  6.52002E-03 0.00046  1.48137E-02 0.00123 ];
RABSXS                    (idx, [1:   6]) = [  7.72821E-03 0.00049  6.51151E-03 0.00046  1.48137E-02 0.00123 ];
ELAXS                     (idx, [1:   6]) = [  2.98272E-01 0.00011  2.96625E-01 0.00012  3.07866E-01 0.00021 ];
INELAXS                   (idx, [1:   6]) = [  5.33758E-03 0.00071  6.25449E-03 0.00068  1.21678E-17 0.00070 ];
SCATTXS                   (idx, [1:   6]) = [  3.03609E-01 0.00010  3.02879E-01 0.00012  3.07866E-01 0.00021 ];
SCATTPRODXS               (idx, [1:   6]) = [  3.03616E-01 0.00010  3.02888E-01 0.00012  3.07866E-01 0.00021 ];
REMXS                     (idx, [1:   6]) = [  7.72937E-03 0.00139  9.05891E-03 0.00129  1.48329E-02 0.00209 ];
NUBAR                     (idx, [1:   6]) = [  2.35795E+00 0.00198  2.35795E+00 0.00198  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  9.44828E-05 0.00285  1.10714E-04 0.00285  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  8.14534E-08 0.00159  8.20105E-09 0.00052  5.07772E-07 0.00123 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.91585E-01 1.5E-05  0.00000E+00 0.0E+00  8.41457E-03 0.00172  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  3.00332E-01 0.00013  0.00000E+00 0.0E+00  2.54855E-03 0.00171  3.07847E-01 0.00023 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.91612E-01 1.5E-05  0.00000E+00 0.0E+00  8.41457E-03 0.00172  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  3.00340E-01 0.00013  0.00000E+00 0.0E+00  2.54855E-03 0.00171  3.07847E-01 0.00023 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  3.03608E-01 0.00011  3.02881E-01 0.00012  3.07847E-01 0.00023 ];
SCATT1                    (idx, [1:   6]) = [  3.66032E-02 0.00072  3.80734E-02 0.00076  2.80476E-02 0.00247 ];
SCATT2                    (idx, [1:   6]) = [  1.30019E-02 0.00158  1.37063E-02 0.00164  8.90197E-03 0.00573 ];
SCATT3                    (idx, [1:   6]) = [  1.44726E-03 0.01238  1.53095E-03 0.01279  9.58885E-04 0.04733 ];
SCATT4                    (idx, [1:   6]) = [ -4.65055E-04 0.03251 -3.57993E-04 0.04570 -1.08837E-03 0.03666 ];
SCATT5                    (idx, [1:   6]) = [  2.18398E-04 0.06195  3.09671E-04 0.04680 -3.11332E-04 0.11391 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.74741E-01 0.00016  2.71326E-01 0.00018  2.94632E-01 0.00037 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.21329E+00 0.00016  1.22858E+00 0.00018  1.13151E+00 0.00037 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.20562E-01 0.00073  1.25707E-01 0.00077  9.11194E-02 0.00251 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.22434E-02 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -6.29768E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.57907E-01 0.0E+00  2.52753E-01 0.0E+00  2.92643E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.29246E+00 0.0E+00  1.31881E+00 0.0E+00  1.13905E+00 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98267 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '347' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  1.09907E+17 0.00069  9.13098E+16 0.00072  1.85975E+16 0.00139 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  3.13347E-01 0.00012  3.11380E-01 0.00014  3.23018E-01 0.00025 ];
FISSXS                    (idx, [1:   6]) = [  3.50728E-05 0.00271  4.22159E-05 0.00269  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  8.11280E-03 0.00060  6.72402E-03 0.00056  1.49367E-02 0.00139 ];
ABSXS                     (idx, [1:   6]) = [  8.14787E-03 0.00060  6.76624E-03 0.00055  1.49367E-02 0.00139 ];
RABSXS                    (idx, [1:   6]) = [  8.14144E-03 0.00060  6.75850E-03 0.00055  1.49367E-02 0.00139 ];
ELAXS                     (idx, [1:   6]) = [  3.00376E-01 0.00013  2.98808E-01 0.00014  3.08081E-01 0.00023 ];
INELAXS                   (idx, [1:   6]) = [  4.82315E-03 0.00091  5.80545E-03 0.00088  1.20619E-17 0.00080 ];
SCATTXS                   (idx, [1:   6]) = [  3.05199E-01 0.00012  3.04613E-01 0.00014  3.08081E-01 0.00023 ];
SCATTPRODXS               (idx, [1:   6]) = [  3.05205E-01 0.00012  3.04621E-01 0.00014  3.08081E-01 0.00023 ];
REMXS                     (idx, [1:   6]) = [  8.14572E-03 0.00158  9.54043E-03 0.00145  1.49317E-02 0.00241 ];
NUBAR                     (idx, [1:   6]) = [  2.30848E+00 0.00556  2.30848E+00 0.00556  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  8.10780E-05 0.00621  9.75936E-05 0.00621  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  9.74628E-08 0.00170  8.67760E-09 0.00063  5.33306E-07 0.00130 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.90890E-01 1.8E-05  0.00000E+00 0.0E+00  9.10950E-03 0.00194  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  3.01831E-01 0.00015  0.00000E+00 0.0E+00  2.77474E-03 0.00193  3.08086E-01 0.00026 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.90917E-01 1.8E-05  0.00000E+00 0.0E+00  9.10950E-03 0.00194  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  3.01839E-01 0.00015  0.00000E+00 0.0E+00  2.77474E-03 0.00193  3.08086E-01 0.00026 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  3.05194E-01 0.00013  3.04606E-01 0.00014  3.08086E-01 0.00026 ];
SCATT1                    (idx, [1:   6]) = [  3.59587E-02 0.00093  3.75697E-02 0.00098  2.80508E-02 0.00275 ];
SCATT2                    (idx, [1:   6]) = [  1.26385E-02 0.00192  1.34131E-02 0.00202  8.83698E-03 0.00651 ];
SCATT3                    (idx, [1:   6]) = [  1.31341E-03 0.01606  1.38026E-03 0.01712  9.86212E-04 0.05042 ];
SCATT4                    (idx, [1:   6]) = [ -5.73397E-04 0.03206 -4.57286E-04 0.04383 -1.14732E-03 0.03897 ];
SCATT5                    (idx, [1:   6]) = [  1.46558E-04 0.10887  2.47795E-04 0.07062 -3.46998E-04 0.11050 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.77388E-01 0.00019  2.73810E-01 0.00022  2.94967E-01 0.00040 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.20173E+00 0.00019  1.21745E+00 0.00022  1.13025E+00 0.00040 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.17825E-01 0.00095  1.23343E-01 0.00100  9.10561E-02 0.00277 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  1.02561E-02 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -6.71090E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.61719E-01 0.0E+00  2.56162E-01 0.0E+00  2.92912E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.27363E+00 0.0E+00  1.30126E+00 0.0E+00  1.13800E+00 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98266 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '348' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  7.47365E+16 0.00081  6.04627E+16 0.00086  1.42738E+16 0.00160 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  3.14984E-01 0.00015  3.12965E-01 0.00018  3.23551E-01 0.00028 ];
FISSXS                    (idx, [1:   6]) = [  3.13688E-05 0.00347  3.87746E-05 0.00346  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  8.50368E-03 0.00071  6.94857E-03 0.00070  1.50961E-02 0.00154 ];
ABSXS                     (idx, [1:   6]) = [  8.53505E-03 0.00071  6.98735E-03 0.00069  1.50961E-02 0.00154 ];
RABSXS                    (idx, [1:   6]) = [  8.52909E-03 0.00071  6.97999E-03 0.00069  1.50961E-02 0.00154 ];
ELAXS                     (idx, [1:   6]) = [  3.02037E-01 0.00015  3.00524E-01 0.00018  3.08455E-01 0.00026 ];
INELAXS                   (idx, [1:   6]) = [  4.41223E-03 0.00113  5.45384E-03 0.00109  1.19387E-17 0.00089 ];
SCATTXS                   (idx, [1:   6]) = [  3.06449E-01 0.00015  3.05978E-01 0.00017  3.08455E-01 0.00026 ];
SCATTPRODXS               (idx, [1:   6]) = [  3.06455E-01 0.00015  3.05985E-01 0.00017  3.08455E-01 0.00026 ];
REMXS                     (idx, [1:   6]) = [  8.51902E-03 0.00183  9.94055E-03 0.00183  1.51343E-02 0.00277 ];
NUBAR                     (idx, [1:   6]) = [  2.10674E+00 0.01150  2.10674E+00 0.01150  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  6.63373E-05 0.01209  8.19960E-05 0.01208  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  1.13575E-07 0.00197  9.10633E-09 0.00075  5.55983E-07 0.00147 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.90264E-01 2.2E-05  0.00000E+00 0.0E+00  9.73590E-03 0.00226  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  3.03017E-01 0.00019  0.00000E+00 0.0E+00  2.97899E-03 0.00225  3.08417E-01 0.00029 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.90290E-01 2.2E-05  0.00000E+00 0.0E+00  9.73590E-03 0.00226  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  3.03025E-01 0.00019  0.00000E+00 0.0E+00  2.97899E-03 0.00225  3.08417E-01 0.00029 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  3.06459E-01 0.00016  3.05996E-01 0.00018  3.08417E-01 0.00029 ];
SCATT1                    (idx, [1:   6]) = [  3.52582E-02 0.00113  3.70056E-02 0.00117  2.78514E-02 0.00325 ];
SCATT2                    (idx, [1:   6]) = [  1.22970E-02 0.00249  1.31051E-02 0.00256  8.87539E-03 0.00797 ];
SCATT3                    (idx, [1:   6]) = [  1.22848E-03 0.02101  1.30094E-03 0.02201  9.18913E-04 0.06278 ];
SCATT4                    (idx, [1:   6]) = [ -6.44109E-04 0.03515 -5.52454E-04 0.04639 -1.03694E-03 0.04946 ];
SCATT5                    (idx, [1:   6]) = [  1.55178E-04 0.13224  2.64687E-04 0.08595 -3.10349E-04 0.14828 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.79726E-01 0.00023  2.75960E-01 0.00026  2.95699E-01 0.00047 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.19171E+00 0.00023  1.20799E+00 0.00026  1.12752E+00 0.00047 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.15054E-01 0.00114  1.20940E-01 0.00119  9.03228E-02 0.00330 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  8.53579E-03 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -7.10099E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.65030E-01 0.0E+00  2.59093E-01 0.0E+00  2.93516E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.25772E+00 0.0E+00  1.28654E+00 0.0E+00  1.13566E+00 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98266 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '349' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  5.02431E+16 0.00099  3.95715E+16 0.00105  1.06716E+16 0.00184 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  3.16412E-01 0.00018  3.14402E-01 0.00021  3.23895E-01 0.00033 ];
FISSXS                    (idx, [1:   6]) = [  2.86159E-05 0.00431  3.63311E-05 0.00429  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  8.85489E-03 0.00084  7.15821E-03 0.00083  1.51556E-02 0.00175 ];
ABSXS                     (idx, [1:   6]) = [  8.88351E-03 0.00084  7.19454E-03 0.00083  1.51556E-02 0.00175 ];
RABSXS                    (idx, [1:   6]) = [  8.87801E-03 0.00084  7.18756E-03 0.00083  1.51556E-02 0.00175 ];
ELAXS                     (idx, [1:   6]) = [  3.03471E-01 0.00019  3.02055E-01 0.00022  3.08739E-01 0.00030 ];
INELAXS                   (idx, [1:   6]) = [  4.05778E-03 0.00149  5.15189E-03 0.00142  1.19475E-17 0.00106 ];
SCATTXS                   (idx, [1:   6]) = [  3.07529E-01 0.00018  3.07207E-01 0.00021  3.08739E-01 0.00030 ];
SCATTPRODXS               (idx, [1:   6]) = [  3.07534E-01 0.00018  3.07214E-01 0.00021  3.08739E-01 0.00030 ];
REMXS                     (idx, [1:   6]) = [  8.86906E-03 0.00224  1.03855E-02 0.00217  1.51009E-02 0.00324 ];
NUBAR                     (idx, [1:   6]) = [  1.79151E+00 0.01829  1.79151E+00 0.01829  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  5.16293E-05 0.01899  6.55706E-05 0.01898  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  1.29714E-07 0.00217  9.51923E-09 0.00095  5.75338E-07 0.00164 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.89609E-01 2.9E-05  0.00000E+00 0.0E+00  1.03910E-02 0.00277  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  3.04010E-01 0.00023  0.00000E+00 0.0E+00  3.19187E-03 0.00275  3.08794E-01 0.00034 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.89629E-01 2.9E-05  0.00000E+00 0.0E+00  1.03910E-02 0.00277  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  3.04016E-01 0.00023  0.00000E+00 0.0E+00  3.19187E-03 0.00275  3.08794E-01 0.00034 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  3.07538E-01 0.00020  3.07202E-01 0.00023  3.08794E-01 0.00034 ];
SCATT1                    (idx, [1:   6]) = [  3.47914E-02 0.00136  3.66686E-02 0.00144  2.78263E-02 0.00365 ];
SCATT2                    (idx, [1:   6]) = [  1.20327E-02 0.00304  1.28868E-02 0.00315  8.86870E-03 0.00881 ];
SCATT3                    (idx, [1:   6]) = [  1.15290E-03 0.02656  1.17336E-03 0.02920  1.07768E-03 0.06264 ];
SCATT4                    (idx, [1:   6]) = [ -6.96764E-04 0.04069 -5.96063E-04 0.05335 -1.06692E-03 0.05415 ];
SCATT5                    (idx, [1:   6]) = [  9.19452E-05 0.26542  2.07213E-04 0.13073 -3.30879E-04 0.16290 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.81621E-01 0.00028  2.77733E-01 0.00032  2.96068E-01 0.00054 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.18372E+00 0.00028  1.20031E+00 0.00032  1.12619E+00 0.00054 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.13134E-01 0.00138  1.19370E-01 0.00146  9.01366E-02 0.00371 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  7.56587E-03 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -7.44787E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.67854E-01 0.0E+00  2.61610E-01 0.0E+00  2.93858E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.24446E+00 0.0E+00  1.27416E+00 0.0E+00  1.13434E+00 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98266 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '350' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  3.33713E+16 0.00117  2.56278E+16 0.00127  7.74354E+15 0.00215 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  3.17563E-01 0.00023  3.15612E-01 0.00027  3.24056E-01 0.00038 ];
FISSXS                    (idx, [1:   6]) = [  2.60820E-05 0.00568  3.39628E-05 0.00566  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  9.15625E-03 0.00106  7.32941E-03 0.00111  1.52144E-02 0.00205 ];
ABSXS                     (idx, [1:   6]) = [  9.18234E-03 0.00106  7.36338E-03 0.00110  1.52144E-02 0.00205 ];
RABSXS                    (idx, [1:   6]) = [  9.17697E-03 0.00106  7.35639E-03 0.00110  1.52144E-02 0.00205 ];
ELAXS                     (idx, [1:   6]) = [  3.04623E-01 0.00023  3.03355E-01 0.00027  3.08842E-01 0.00035 ];
INELAXS                   (idx, [1:   6]) = [  3.75835E-03 0.00194  4.89352E-03 0.00182  1.19365E-17 0.00126 ];
SCATTXS                   (idx, [1:   6]) = [  3.08381E-01 0.00022  3.08249E-01 0.00026  3.08842E-01 0.00035 ];
SCATTPRODXS               (idx, [1:   6]) = [  3.08386E-01 0.00022  3.08256E-01 0.00026  3.08842E-01 0.00035 ];
REMXS                     (idx, [1:   6]) = [  9.19521E-03 0.00267  1.07186E-02 0.00262  1.52532E-02 0.00365 ];
NUBAR                     (idx, [1:   6]) = [  1.30508E+00 0.02896  1.30508E+00 0.02896  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  3.43380E-05 0.03003  4.46989E-05 0.03003  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  1.45326E-07 0.00261  9.87133E-09 0.00121  5.93477E-07 0.00198 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.89141E-01 3.7E-05  0.00000E+00 0.0E+00  1.08590E-02 0.00339  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  3.04887E-01 0.00028  0.00000E+00 0.0E+00  3.34688E-03 0.00337  3.08803E-01 0.00040 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.89162E-01 3.7E-05  0.00000E+00 0.0E+00  1.08590E-02 0.00339  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  3.04894E-01 0.00028  0.00000E+00 0.0E+00  3.34688E-03 0.00337  3.08803E-01 0.00040 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  3.08363E-01 0.00024  3.08234E-01 0.00028  3.08803E-01 0.00040 ];
SCATT1                    (idx, [1:   6]) = [  3.43410E-02 0.00166  3.63070E-02 0.00179  2.78162E-02 0.00431 ];
SCATT2                    (idx, [1:   6]) = [  1.17956E-02 0.00371  1.27110E-02 0.00397  8.75904E-03 0.01035 ];
SCATT3                    (idx, [1:   6]) = [  1.14562E-03 0.03432  1.13956E-03 0.03897  1.15813E-03 0.07177 ];
SCATT4                    (idx, [1:   6]) = [ -7.03848E-04 0.04765 -6.52963E-04 0.05820 -8.67286E-04 0.07559 ];
SCATT5                    (idx, [1:   6]) = [  4.93754E-05 0.60104  1.48851E-04 0.22989 -2.80917E-04 0.20890 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.83222E-01 0.00034  2.79305E-01 0.00041  2.96240E-01 0.00062 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.17707E+00 0.00034  1.19364E+00 0.00041  1.12564E+00 0.00062 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.11375E-01 0.00169  1.17805E-01 0.00184  9.01055E-02 0.00436 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  6.37973E-03 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -7.75083E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.70185E-01 0.0E+00  2.63746E-01 0.0E+00  2.93933E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.23372E+00 0.0E+00  1.26384E+00 0.0E+00  1.13404E+00 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98266 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '351' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  2.19083E+16 0.00143  1.64002E+16 0.00157  5.50803E+15 0.00254 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  3.18272E-01 0.00028  3.16191E-01 0.00033  3.24512E-01 0.00045 ];
FISSXS                    (idx, [1:   6]) = [  2.42212E-05 0.00717  3.23493E-05 0.00711  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  9.45849E-03 0.00133  7.46749E-03 0.00134  1.53997E-02 0.00238 ];
ABSXS                     (idx, [1:   6]) = [  9.48271E-03 0.00132  7.49984E-03 0.00133  1.53997E-02 0.00238 ];
RABSXS                    (idx, [1:   6]) = [  9.47759E-03 0.00132  7.49300E-03 0.00134  1.53997E-02 0.00238 ];
ELAXS                     (idx, [1:   6]) = [  3.05275E-01 0.00028  3.03997E-01 0.00034  3.09112E-01 0.00042 ];
INELAXS                   (idx, [1:   6]) = [  3.51447E-03 0.00247  4.69396E-03 0.00231  1.21021E-17 0.00146 ];
SCATTXS                   (idx, [1:   6]) = [  3.08790E-01 0.00027  3.08691E-01 0.00033  3.09112E-01 0.00042 ];
SCATTPRODXS               (idx, [1:   6]) = [  3.08795E-01 0.00027  3.08697E-01 0.00033  3.09112E-01 0.00042 ];
REMXS                     (idx, [1:   6]) = [  9.51295E-03 0.00309  1.10652E-02 0.00315  1.54678E-02 0.00408 ];
NUBAR                     (idx, [1:   6]) = [  9.51530E-01 0.03897  9.51530E-01 0.03897  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  2.41102E-05 0.04056  3.21748E-05 0.04054  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  1.61008E-07 0.00303  1.01785E-08 0.00142  6.09925E-07 0.00226 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.88520E-01 4.7E-05  0.00000E+00 0.0E+00  1.14805E-02 0.00407  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  3.05118E-01 0.00035  0.00000E+00 0.0E+00  3.54301E-03 0.00404  3.09044E-01 0.00046 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.88542E-01 4.7E-05  0.00000E+00 0.0E+00  1.14805E-02 0.00407  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  3.05125E-01 0.00035  0.00000E+00 0.0E+00  3.54301E-03 0.00404  3.09044E-01 0.00046 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  3.08754E-01 0.00029  3.08661E-01 0.00034  3.09044E-01 0.00046 ];
SCATT1                    (idx, [1:   6]) = [  3.39980E-02 0.00217  3.60993E-02 0.00234  2.77391E-02 0.00497 ];
SCATT2                    (idx, [1:   6]) = [  1.15509E-02 0.00495  1.24800E-02 0.00526  8.77552E-03 0.01249 ];
SCATT3                    (idx, [1:   6]) = [  1.07088E-03 0.04363  1.05391E-03 0.05176  1.12213E-03 0.08130 ];
SCATT4                    (idx, [1:   6]) = [ -7.36017E-04 0.05523 -7.10952E-04 0.06713 -8.13792E-04 0.09910 ];
SCATT5                    (idx, [1:   6]) = [  1.24368E-04 0.31132  2.25284E-04 0.19782 -1.79203E-04 0.42723 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.84274E-01 0.00043  2.80091E-01 0.00052  2.96772E-01 0.00072 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.17280E+00 0.00043  1.19041E+00 0.00052  1.12377E+00 0.00072 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.10128E-01 0.00221  1.16977E-01 0.00239  8.97896E-02 0.00502 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  6.25214E-03 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -8.03482E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.71750E-01 0.0E+00  2.64895E-01 0.0E+00  2.94437E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.22662E+00 0.0E+00  1.25836E+00 0.0E+00  1.13210E+00 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98266 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '352' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  1.41743E+16 0.00181  1.03663E+16 0.00199  3.80804E+15 0.00306 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  3.18908E-01 0.00033  3.16770E-01 0.00041  3.24797E-01 0.00055 ];
FISSXS                    (idx, [1:   6]) = [  2.28091E-05 0.00930  3.11802E-05 0.00923  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  9.66265E-03 0.00155  7.57853E-03 0.00167  1.53584E-02 0.00282 ];
ABSXS                     (idx, [1:   6]) = [  9.68546E-03 0.00155  7.60971E-03 0.00165  1.53584E-02 0.00282 ];
RABSXS                    (idx, [1:   6]) = [  9.68099E-03 0.00155  7.60361E-03 0.00166  1.53584E-02 0.00282 ];
ELAXS                     (idx, [1:   6]) = [  3.05894E-01 0.00034  3.04611E-01 0.00042  3.09438E-01 0.00051 ];
INELAXS                   (idx, [1:   6]) = [  3.32833E-03 0.00313  4.54992E-03 0.00293  1.20859E-17 0.00176 ];
SCATTXS                   (idx, [1:   6]) = [  3.09222E-01 0.00032  3.09160E-01 0.00040  3.09438E-01 0.00051 ];
SCATTPRODXS               (idx, [1:   6]) = [  3.09227E-01 0.00032  3.09167E-01 0.00040  3.09438E-01 0.00051 ];
REMXS                     (idx, [1:   6]) = [  9.61409E-03 0.00383  1.12305E-02 0.00396  1.53774E-02 0.00525 ];
NUBAR                     (idx, [1:   6]) = [  6.06436E-01 0.05467  6.06436E-01 0.05467  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  1.46898E-05 0.05795  2.00682E-05 0.05790  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  1.74245E-07 0.00370  1.04786E-08 0.00177  6.19583E-07 0.00275 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.87985E-01 6.1E-05  0.00000E+00 0.0E+00  1.20153E-02 0.00502  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  3.05533E-01 0.00043  0.00000E+00 0.0E+00  3.71515E-03 0.00501  3.09419E-01 0.00058 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.88007E-01 6.1E-05  0.00000E+00 0.0E+00  1.20153E-02 0.00502  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  3.05540E-01 0.00043  0.00000E+00 0.0E+00  3.71515E-03 0.00501  3.09419E-01 0.00058 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  3.09289E-01 0.00035  3.09248E-01 0.00043  3.09419E-01 0.00058 ];
SCATT1                    (idx, [1:   6]) = [  3.37053E-02 0.00266  3.59463E-02 0.00297  2.75937E-02 0.00598 ];
SCATT2                    (idx, [1:   6]) = [  1.14484E-02 0.00597  1.24830E-02 0.00649  8.62355E-03 0.01554 ];
SCATT3                    (idx, [1:   6]) = [  1.03894E-03 0.05577  9.64076E-04 0.06905  1.24896E-03 0.08986 ];
SCATT4                    (idx, [1:   6]) = [ -8.53811E-04 0.05922 -8.24504E-04 0.07269 -9.29077E-04 0.10608 ];
SCATT5                    (idx, [1:   6]) = [  5.59991E-05 0.80941  1.52319E-04 0.34627 -2.04995E-04 0.45038 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.85202E-01 0.00052  2.80824E-01 0.00062  2.97203E-01 0.00087 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.16907E+00 0.00052  1.18744E+00 0.00062  1.12241E+00 0.00087 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.08997E-01 0.00271  1.16262E-01 0.00301  8.92285E-02 0.00606 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  5.14377E-03 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -8.24109E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.73241E-01 0.0E+00  2.66089E-01 0.0E+00  2.94810E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.21992E+00 0.0E+00  1.25271E+00 0.0E+00  1.13067E+00 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98266 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '353' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  8.88647E+15 0.00221  6.36967E+15 0.00249  2.51679E+15 0.00367 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  3.19473E-01 0.00042  3.17312E-01 0.00053  3.25056E-01 0.00066 ];
FISSXS                    (idx, [1:   6]) = [  2.25507E-05 0.01197  3.14794E-05 0.01197  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  9.89376E-03 0.00198  7.69685E-03 0.00217  1.54852E-02 0.00340 ];
ABSXS                     (idx, [1:   6]) = [  9.91631E-03 0.00197  7.72833E-03 0.00215  1.54852E-02 0.00340 ];
RABSXS                    (idx, [1:   6]) = [  9.91141E-03 0.00197  7.72147E-03 0.00215  1.54852E-02 0.00340 ];
ELAXS                     (idx, [1:   6]) = [  3.06348E-01 0.00042  3.05108E-01 0.00053  3.09570E-01 0.00061 ];
INELAXS                   (idx, [1:   6]) = [  3.20871E-03 0.00400  4.47604E-03 0.00380  1.20505E-17 0.00218 ];
SCATTXS                   (idx, [1:   6]) = [  3.09557E-01 0.00041  3.09584E-01 0.00051  3.09570E-01 0.00061 ];
SCATTPRODXS               (idx, [1:   6]) = [  3.09562E-01 0.00041  3.09590E-01 0.00051  3.09570E-01 0.00061 ];
REMXS                     (idx, [1:   6]) = [  9.93427E-03 0.00468  1.14937E-02 0.00483  1.55877E-02 0.00636 ];
NUBAR                     (idx, [1:   6]) = [  3.86904E-01 0.07277  3.86904E-01 0.07277  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  9.28831E-06 0.07922  1.29539E-05 0.07938  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  1.87345E-07 0.00440  1.06687E-08 0.00220  6.34035E-07 0.00333 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.87833E-01 8.4E-05  0.00000E+00 0.0E+00  1.21667E-02 0.00679  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  3.05812E-01 0.00057  0.00000E+00 0.0E+00  3.76402E-03 0.00671  3.09468E-01 0.00070 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.87853E-01 8.4E-05  0.00000E+00 0.0E+00  1.21667E-02 0.00679  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  3.05818E-01 0.00057  0.00000E+00 0.0E+00  3.76402E-03 0.00671  3.09468E-01 0.00070 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  3.09534E-01 0.00044  3.09576E-01 0.00055  3.09468E-01 0.00070 ];
SCATT1                    (idx, [1:   6]) = [  3.32846E-02 0.00341  3.55450E-02 0.00383  2.75443E-02 0.00750 ];
SCATT2                    (idx, [1:   6]) = [  1.13527E-02 0.00767  1.23987E-02 0.00811  8.69694E-03 0.01913 ];
SCATT3                    (idx, [1:   6]) = [  9.96841E-04 0.07400  9.40124E-04 0.09343  1.15960E-03 0.11910 ];
SCATT4                    (idx, [1:   6]) = [ -8.31927E-04 0.07993 -8.67983E-04 0.09133 -7.32005E-04 0.16553 ];
SCATT5                    (idx, [1:   6]) = [  7.91554E-05 0.74954  2.55705E-04 0.27613 -3.72124E-04 0.30159 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.86189E-01 0.00065  2.81767E-01 0.00079  2.97511E-01 0.00108 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.16523E+00 0.00065  1.18375E+00 0.00079  1.12171E+00 0.00108 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.07564E-01 0.00347  1.14859E-01 0.00388  8.90975E-02 0.00761 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  5.09153E-03 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -8.46671E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.74207E-01 0.0E+00  2.66752E-01 0.0E+00  2.95076E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.21563E+00 0.0E+00  1.24960E+00 0.0E+00  1.12965E+00 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98266 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '354' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  5.18872E+15 0.00273  3.66525E+15 0.00312  1.52347E+15 0.00455 ];
LEAK                      (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOTXS                     (idx, [1:   6]) = [  3.19315E-01 0.00053  3.16812E-01 0.00068  3.25508E-01 0.00086 ];
FISSXS                    (idx, [1:   6]) = [  2.32991E-05 0.01515  3.30333E-05 0.01518  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  1.00118E-02 0.00261  7.70868E-03 0.00278  1.55959E-02 0.00451 ];
ABSXS                     (idx, [1:   6]) = [  1.00351E-02 0.00260  7.74171E-03 0.00276  1.55959E-02 0.00451 ];
RABSXS                    (idx, [1:   6]) = [  1.00296E-02 0.00261  7.73384E-03 0.00277  1.55959E-02 0.00451 ];
ELAXS                     (idx, [1:   6]) = [  3.06083E-01 0.00053  3.04545E-01 0.00069  3.09912E-01 0.00079 ];
INELAXS                   (idx, [1:   6]) = [  3.19649E-03 0.00514  4.52519E-03 0.00491  1.18935E-17 0.00283 ];
SCATTXS                   (idx, [1:   6]) = [  3.09280E-01 0.00051  3.09071E-01 0.00066  3.09912E-01 0.00079 ];
SCATTPRODXS               (idx, [1:   6]) = [  3.09285E-01 0.00051  3.09079E-01 0.00066  3.09912E-01 0.00079 ];
REMXS                     (idx, [1:   6]) = [  9.95562E-03 0.00613  1.16222E-02 0.00632  1.55765E-02 0.00811 ];
NUBAR                     (idx, [1:   6]) = [  2.85871E-01 0.08669  2.85871E-01 0.08669  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  8.13893E-06 0.09729  1.15480E-05 0.09727  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  1.96204E-07 0.00560  1.08073E-08 0.00287  6.41749E-07 0.00440 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.87170E-01 0.00011  0.00000E+00 0.0E+00  1.28302E-02 0.00840  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  3.05182E-01 0.00073  0.00000E+00 0.0E+00  3.96291E-03 0.00831  3.09931E-01 0.00089 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.87196E-01 0.00011  0.00000E+00 0.0E+00  1.28302E-02 0.00840  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  3.05190E-01 0.00073  0.00000E+00 0.0E+00  3.96291E-03 0.00831  3.09931E-01 0.00089 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  3.09353E-01 0.00055  3.09145E-01 0.00070  3.09931E-01 0.00089 ];
SCATT1                    (idx, [1:   6]) = [  3.33591E-02 0.00448  3.58459E-02 0.00501  2.73825E-02 0.00974 ];
SCATT2                    (idx, [1:   6]) = [  1.12037E-02 0.00997  1.22639E-02 0.01064  8.67431E-03 0.02437 ];
SCATT3                    (idx, [1:   6]) = [  1.01710E-03 0.09311  8.81464E-04 0.12843  1.34140E-03 0.12811 ];
SCATT4                    (idx, [1:   6]) = [ -7.86739E-04 0.10802 -7.23667E-04 0.14154 -9.33990E-04 0.16804 ];
SCATT5                    (idx, [1:   6]) = [ -7.91046E-05 0.95261  4.62758E-05 1.90688 -3.97586E-04 0.36501 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.85956E-01 0.00085  2.80966E-01 0.00107  2.98125E-01 0.00140 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.16652E+00 0.00085  1.18773E+00 0.00107  1.12029E+00 0.00140 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.07893E-01 0.00456  1.16042E-01 0.00512  8.84910E-02 0.00986 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  5.99899E-03 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -8.54845E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.74085E-01 0.0E+00  2.66082E-01 0.0E+00  2.95463E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.21617E+00 0.0E+00  1.25275E+00 0.0E+00  1.12817E+00 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.10' ;
TITLE                     (idx, [1: 22])  = 'ADF project with DYN3D' ;
START_DATE                (idx, [1: 24])  = 'Wed Feb 27 20:27:48 2013' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Feb 28 04:27:01 2013' ;

% Run parameters:

POP                       (idx, 1)        = 400000 ;
CYCLES                    (idx, 1)        = 1000 ;
SKIP                      (idx, 1)        = 200 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1361993268 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, 1)        = 1 ;
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 30])  = 'AMD Opteron(TM) Processor 6276' ;
CPU_MHZ                   (idx, 1)        = 2300.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 64 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  64]) = [  9.99029E-01  1.00507E+00  1.00058E+00  1.00158E+00  1.00077E+00  9.97492E-01  1.00180E+00  1.00187E+00  1.00271E+00  1.00292E+00  9.99981E-01  9.94859E-01  1.00076E+00  9.99106E-01  9.99727E-01  9.99643E-01  1.00339E+00  9.99754E-01  1.00408E+00  1.00573E+00  9.97642E-01  9.98603E-01  9.97010E-01  1.00493E+00  1.00390E+00  1.00679E+00  9.94934E-01  9.96175E-01  1.00179E+00  9.94007E-01  9.94813E-01  1.00095E+00  1.00473E+00  1.00588E+00  1.00264E+00  9.94730E-01  9.96355E-01  9.97817E-01  1.00054E+00  1.00050E+00  1.00207E+00  1.00739E+00  1.00291E+00  1.00204E+00  1.00110E+00  9.97146E-01  1.00020E+00  1.00051E+00  1.00054E+00  9.99746E-01  9.95499E-01  9.98230E-01  1.00145E+00  9.93356E-01  9.95222E-01  9.96465E-01  9.97078E-01  1.00517E+00  9.99562E-01  9.95483E-01  1.00238E+00  9.94356E-01  9.98996E-01  9.97485E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 61])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/fridman/serpent/install/xsdata/jeff31/sss_jeff31.nfy' ;
IBR_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:  2])  = [  1.77047E-01  0.00000E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  6.16700E-02 7.1E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.38330E-01 4.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.31653E-01 1.5E-05  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  4.32092E-01 1.5E-05  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 1000 ;
SOURCE_NEUTRONS           (idx, 1)        = 480133783 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  4.00000E+05 0.00009 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.58698E+04 ;
RUNNING_TIME              (idx, 1)        =  4.79224E+02 ;
INIT_TIME                 (idx, 1)        =  1.37883E-01 ;
PROCESS_TIME              (idx, [1:  2])  = [  1.59833E-02  1.59833E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  2])  = [  4.79069E+02  4.79069E+02 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.79221E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 53.98266 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.50796E+01 0.00071 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.44276E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 5.92 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 258344.94 ;
ALLOC_MEMSIZE             (idx, 1)        = 622.98;
MEMSIZE                   (idx, 1)        = 547.03;
XS_MEMSIZE                (idx, 1)        = 207.99;
MAT_MEMSIZE               (idx, 1)        = 77.49;
RES_MEMSIZE               (idx, 1)        = 14.94;
MISC_MEMSIZE              (idx, 1)        = 246.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 75.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 50 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 46423 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Photon energy grid:

PHOTON_EMIN               (idx, 1)        =  1.00000E+37 ;
PHOTON_EMAX               (idx, 1)        = -1.00000E+37 ;

% Unresolved reso0ce probability table sampling:

URES_DILU_CUT             (idx, 1)        =  0.00000E+00 ;
URES_EMIN                 (idx, 1)        =  1.50000E-04 ;
URES_EMAX                 (idx, 1)        =  1.50000E-01 ;
URES_AVAIL                (idx, 1)        = 6 ;
URES_USED                 (idx, 1)        = 2 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 56 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 56 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 404 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_MODE              (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  4.11140E+12 ;
TOT_DECAY_HEAT            (idx, 1)        =  3.23609E+00 ;
TOT_SF_RATE               (idx, 1)        =  1.67901E-02 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  4.11140E+12 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  3.23609E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  3.95898E+07 ;
INGESTION_TOXICITY        (idx, 1)        =  2.09896E+05 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  1.13797E+00 0.00011 ];
TH232_FISS_FRAC           (idx, [1:   2]) = [  3.95833E-02 0.00039 ];
U233_FISS_FRAC            (idx, [1:   2]) = [  9.60417E-01 1.6E-05 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  5.45300E+06 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.77550E-02 3.9E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  4.28687E+17 3.1E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.70880E+17 4.5E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.43698E+17 5.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  4.14577E+17 3.1E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  4.13393E+17 5.9E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.48280E+19 5.3E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75113E+14 0.00246 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  4.14752E+17 3.1E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.38994E+19 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  3.07125E+02 ;
TOT_FMASS                 (idx, 1)        =  3.07125E+02 ;

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.03703E+00 6.2E-05  1.03355E+00 6.0E-05  3.46566E-03 0.00132 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.03700E+00 5.9E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.03693E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03737E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];

% Inverse neutron velocity :

ANA_INV_SPD               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Analog neutron lifetime (t/p/d):

ANA_LIFETIME              (idx, [1:   6]) = [  3.30966E-06 0.00025  3.31089E-06 0.00025  2.95698E-06 0.00391 ];

% Implicit prompt neutron lifetime:

IMPL_PROMPT_LIFETIME      (idx, [1:   2]) = [  3.30951E-06 0.00024 ];

% Analog and implicit reproduction time:

ANA_REPROD_TIME           (idx, [1:   2]) = [  3.19150E-06 0.00026 ];
IMPL_REPROD_TIME          (idx, [1:   2]) = [  3.20194E-06 0.00025 ];

% Analog and implicit Rossi alpha:

ANA_ROSSI_ALPHA           (idx, [1:   6]) = [ -3.13353E+05 0.00026  1.16419E+04 0.00172 -1.05265E+03 0.00134 ];
IMP_ROSSI_ALPHA           (idx, [1:   2]) = [ -1.05015E+03 0.00135 ];

% Analog and implicit removal times:

ANA_REM_TIME              (idx, [1:  10]) = [  3.30966E-06 0.00025  3.30671E-06 0.00025  1.03040E-05 0.00701  4.28488E-06 0.00030  1.91191E-06 0.00028 ];
IMP_REM_TIME              (idx, [1:  10]) = [  3.30951E-06 0.00024  3.31090E-06 0.00024  7.88649E-03 0.00250  5.63249E-06 0.00023  8.03273E-06 0.00025 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.42414E-06 0.00024  6.42423E-06 0.00024  6.39605E-06 0.00453 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.89631E-05 0.00025  3.89710E-05 0.00025  3.63678E-05 0.00459 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41226E-02 0.00024  5.41457E-02 0.00024  4.74932E-02 0.00400 ];

% Implicit and Analog delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
IMPL_BETA_EFF             (idx, [1:  18]) = [  3.36230E-03 0.00133  2.32885E-04 0.00500  4.64243E-04 0.00342  4.24265E-04 0.00375  6.48203E-04 0.00306  1.08814E-03 0.00234  2.03203E-04 0.00542  2.47029E-04 0.00485  5.43314E-05 0.00995 ];
ANA_BETA_EFF              (idx, [1:  18]) = [  3.35930E-03 0.00132  2.30972E-04 0.00510  4.64154E-04 0.00356  4.25918E-04 0.00383  6.48346E-04 0.00311  1.08591E-03 0.00235  2.03208E-04 0.00557  2.46700E-04 0.00485  5.40951E-05 0.01042 ];
IMPL_BETA_ZERO            (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_BETA_ZERO             (idx, [1:  18]) = [  3.46091E-03 7.9E-05  2.40856E-04 3.1E-05  4.77740E-04 3.5E-05  4.35131E-04 5.5E-05  6.65970E-04 5.2E-05  1.12078E-03 9.5E-05  2.10088E-04 0.00020  2.54141E-04 0.00013  5.62065E-05 0.00015 ];
IMPL_DECAY_CONSTANT       (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
ANA_DECAY_CONSTANT        (idx, [1:  18]) = [  3.48006E-01 0.00217  1.24667E-02 7.2E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 2.7E-09  1.63478E+00 4.2E-09  3.55460E+00 2.8E-09 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.60528E+01 0.00186 ];

% Parameters for group constant generation

GC_UNIVERSE_NAME          (idx, [1:  3])  = '355' ;
GC_NE                     (idx, 1)        = 2 ;
GC_BOUNDS                 (idx, [1:   3]) = [  2.00000E+01  1.48728E-04  1.00000E-11 ];

% Few-group cross sections:

FLUX                      (idx, [1:   6]) = [  2.40287E+15 0.00341  1.69222E+15 0.00400  7.10651E+14 0.00598 ];
LEAK                      (idx, [1:   6]) = [  1.20517E+14 0.00308  8.60832E+13 0.00366  3.44335E+13 0.00580 ];
TOTXS                     (idx, [1:   6]) = [  3.17788E-01 0.00080  3.14691E-01 0.00100  3.25476E-01 0.00132 ];
FISSXS                    (idx, [1:   6]) = [  2.97644E-05 0.02091  4.22608E-05 0.02072  0.00000E+00 0.0E+00 ];
CAPTXS                    (idx, [1:   6]) = [  9.90015E-03 0.00382  7.56553E-03 0.00411  1.55307E-02 0.00662 ];
ABSXS                     (idx, [1:   6]) = [  9.92991E-03 0.00381  7.60779E-03 0.00408  1.55307E-02 0.00662 ];
RABSXS                    (idx, [1:   6]) = [  9.92335E-03 0.00382  7.59848E-03 0.00410  1.55307E-02 0.00662 ];
ELAXS                     (idx, [1:   6]) = [  3.04370E-01 0.00079  3.02130E-01 0.00102  3.09945E-01 0.00121 ];
INELAXS                   (idx, [1:   6]) = [  3.48890E-03 0.00731  4.95364E-03 0.00697  1.20198E-17 0.00414 ];
SCATTXS                   (idx, [1:   6]) = [  3.07858E-01 0.00077  3.07084E-01 0.00098  3.09945E-01 0.00121 ];
SCATTPRODXS               (idx, [1:   6]) = [  3.07865E-01 0.00077  3.07093E-01 0.00098  3.09945E-01 0.00121 ];
REMXS                     (idx, [1:   6]) = [  1.00156E-02 0.00927  1.16038E-02 0.00975  1.57108E-02 0.01177 ];
NUBAR                     (idx, [1:   6]) = [  1.56238E-01 0.11973  1.56238E-01 0.11973  0.00000E+00 0.0E+00 ];
NSF                       (idx, [1:   6]) = [  6.44743E-06 0.13308  9.08082E-06 0.13214  0.00000E+00 0.0E+00 ];
RECIPVEL                  (idx, [1:   6]) = [  1.97397E-07 0.00756  1.07348E-08 0.00413  6.40813E-07 0.00588 ];
FISSE                     (idx, [1:   6]) = [  1.96788E+02 3.1E-09  1.96788E+02 3.1E-09  0.00000E+00 0.0E+00 ];

% Fission spectra:

CHI                       (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHIP                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
CHID                      (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Group-transfer probabilities and cross sections:

GTRANSFP                  (idx, [1:   8]) = [  9.87302E-01 0.00016  0.00000E+00 0.0E+00  1.26979E-02 0.01276  1.00000E+00 0.0E+00 ];
GTRANSFXS                 (idx, [1:   8]) = [  3.03074E-01 0.00109  0.00000E+00 0.0E+00  3.89008E-03 0.01267  3.09765E-01 0.00135 ];

% Group-production probabilities and cross sections:

GPRODP                    (idx, [1:   8]) = [  9.87345E-01 0.00016  0.00000E+00 0.0E+00  1.26979E-02 0.01276  1.00000E+00 0.0E+00 ];
GPRODXS                   (idx, [1:   8]) = [  3.03088E-01 0.00109  0.00000E+00 0.0E+00  3.89008E-03 0.01267  3.09765E-01 0.00135 ];

% PN scattering cross sections:

SCATT0                    (idx, [1:   6]) = [  3.07763E-01 0.00083  3.06964E-01 0.00105  3.09765E-01 0.00135 ];
SCATT1                    (idx, [1:   6]) = [  3.35382E-02 0.00636  3.60874E-02 0.00724  2.74026E-02 0.01479 ];
SCATT2                    (idx, [1:   6]) = [  1.16303E-02 0.01437  1.27805E-02 0.01568  8.94964E-03 0.03523 ];
SCATT3                    (idx, [1:   6]) = [  1.20236E-03 0.11726  1.25322E-03 0.13492  1.09531E-03 0.23763 ];
SCATT4                    (idx, [1:   6]) = [ -6.50627E-04 0.19021 -6.25773E-04 0.23828 -6.89776E-04 0.33047 ];
SCATT5                    (idx, [1:   6]) = [  1.11692E-04 0.98648  3.97130E-04 0.33244 -5.55342E-04 0.39169 ];

% P1 diffusion parameters:

P1_TRANSPXS               (idx, [1:   6]) = [  2.84250E-01 0.00124  2.78604E-01 0.00158  2.98073E-01 0.00216 ];
P1_DIFFCOEF               (idx, [1:   6]) = [  1.17448E+00 0.00124  1.19945E+00 0.00159  1.12348E+00 0.00216 ];
P1_MUBAR                  (idx, [1:   6]) = [  1.09100E-01 0.00647  1.17793E-01 0.00742  8.88460E-02 0.01492 ];

% B1 critical spectrum calculation:

B1_KINF                   (idx, [1:   2]) = [  7.07911E-03 0.0E+00 ];
B1_BUCKLING               (idx, [1:   2]) = [ -8.39128E-03 0.0E+00 ];
B1_FLUX                   (idx, [1:   6]) = [         -0 0.0E+00         -0 0.0E+00         -0 0.0E+00 ];
B1_TOTXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHI                    (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABSXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_RABSXS                 (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   6]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTXS                (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTPRODXS            (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INF_TRANSPXS           (idx, [1:   6]) = [  2.70423E-01 0.0E+00  2.61239E-01 0.0E+00  2.95127E-01 0.0E+00 ];
B1_INF_DIFFCOEF           (idx, [1:   6]) = [  1.23264E+00 0.0E+00  1.27597E+00 0.0E+00  1.12946E+00 0.0E+00 ];

