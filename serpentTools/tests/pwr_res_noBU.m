
% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.30' ;
COMPILE_DATE              (idx, [1: 20])  = 'Apr  4 2018 08:55:27' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1: 13])  = 'UO2 PIN MODEL' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1:  3])  = 'pwr' ;
WORKING_DIRECTORY         (idx, [1: 70])  = '/gpfs/pace1/project/me-kotlyar/dkotlyar6/Research/Serpent_test/FP_test' ;
HOSTNAME                  (idx, [1: 32])  = 'rich133-c36-10-l.pace.gatech.edu' ;
CPU_TYPE                  (idx, [1: 41])  = 'Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz' ;
CPU_MHZ                   (idx, 1)        = 184549409.0 ;
START_DATE                (idx, [1: 24])  = 'Mon May 14 11:20:06 2018' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Mon May 14 11:20:36 2018' ;

% Run parameters:

POP                       (idx, 1)        = 5000 ;
CYCLES                    (idx, 1)        = 100 ;
SKIP                      (idx, 1)        = 10 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1526311206 ;
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
DOUBLE_INDEXING           (idx, 1)        = 0 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 8 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:   8]) = [  9.87692E-01  9.98407E-01  9.99815E-01  1.00577E+00  1.00453E+00  1.00540E+00  1.00143E+00  9.96955E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 53])  = '/nv/hp22/dkotlyar6/data/Codes/DATA/sss_endfb7u.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 49])  = '/nv/hp22/dkotlyar6/data/Codes/DATA/sss_endfb7.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 49])  = '/nv/hp22/dkotlyar6/data/Codes/DATA/sss_endfb7.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 49])  = '/nv/hp22/dkotlyar6/data/Codes/DATA/sss_endfb7.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.62904E-02 0.00343  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.83710E-01 5.7E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  7.06733E-01 0.00021  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  7.07379E-01 0.00021  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.44970E+00 0.00074  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.63979E+01 0.00064  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.63979E+01 0.00064  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.09200E+01 0.00087  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  5.34339E-01 0.00367  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 100 ;
SOURCE_POPULATION         (idx, 1)        = 500170 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  5.00170E+03 0.00232 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  5.00170E+03 0.00232 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  8.28167E-01 ;
RUNNING_TIME              (idx, 1)        =  4.96417E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  2.29467E-01  2.29467E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.00001E-04  1.00001E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  2.66850E-01  2.66850E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.96050E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 1.66829 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  7.97963E+00 0.00301 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  1.96576E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 129078.54 ;
ALLOC_MEMSIZE             (idx, 1)        = 192.75;
MEMSIZE                   (idx, 1)        = 97.97;
XS_MEMSIZE                (idx, 1)        = 33.96;
MAT_MEMSIZE               (idx, 1)        = 6.73;
RES_MEMSIZE               (idx, 1)        = 4.80;
MISC_MEMSIZE              (idx, 1)        = 52.48;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 94.78;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 2 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  5.00000E-05 ;
NEUTRON_ERG_NE            (idx, 1)        = 58536 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-09 ;
NEUTRON_EMAX              (idx, 1)        =  1.50000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  2.00000E-02 ;
URES_EMAX                 (idx, 1)        =  1.49029E-01 ;
URES_AVAIL                (idx, 1)        = 3 ;
URES_USED                 (idx, 1)        = 1 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 7 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 7 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 154 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
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

TOT_ACTIVITY              (idx, 1)        =  7.29422E+04 ;
TOT_DECAY_HEAT            (idx, 1)        =  5.07881E-08 ;
TOT_SF_RATE               (idx, 1)        =  3.14973E+00 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  7.29422E+04 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  5.07881E-08 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  5.91165E-01 ;
INGESTION_TOXICITY        (idx, 1)        =  3.31291E-03 ;
ACTINIDE_INH_TOX          (idx, 1)        =  5.91165E-01 ;
ACTINIDE_ING_TOX          (idx, 1)        =  3.31291E-03 ;
FISSION_PRODUCT_INH_TOX   (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_ING_TOX   (idx, 1)        =  0.00000E+00 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
PHOTON_DECAY_SOURCE       (idx, 1)        =  2.27311E+04 ;
NEUTRON_DECAY_SOURCE      (idx, 1)        =  0.00000E+00 ;
ALPHA_DECAY_SOURCE        (idx, 1)        =  7.27205E+04 ;
ELECTRON_DECAY_SOURCE     (idx, 1)        =  4.16136E+04 ;

% Normalization coefficient:

NORM_COEF                 (idx, [1:   4]) = [  2.42653E+09 0.00172  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  7.19737E-01 0.00298 ];
U235_FISS                 (idx, [1:   4]) = [  5.09108E+12 0.00192  8.98599E-01 0.00068 ];
U238_FISS                 (idx, [1:   4]) = [  5.74658E+11 0.00666  1.01401E-01 0.00599 ];
U235_CAPT                 (idx, [1:   4]) = [  1.46165E+12 0.00436  2.25084E-01 0.00355 ];
U238_CAPT                 (idx, [1:   4]) = [  4.71586E+12 0.00284  7.26201E-01 0.00115 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 500170 5.00000E+05 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.11238E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 500170 5.01112E+05 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 267079 2.67598E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 233091 2.33514E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 500170 5.01112E+05 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 -3.84171E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.83522E+02 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  3.80000E-02 6.7E-09 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.39857E+13 5.3E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  5.64951E+12 6.6E-06 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  6.50911E+12 0.00178 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.21586E+13 0.00095 ];
TOT_SRCRATE               (idx, [1:   2]) = [  1.21327E+13 0.00172 ];
TOT_FLUX                  (idx, [1:   2]) = [  9.19852E+14 0.00147 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.21586E+13 0.00095 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  3.20953E+14 0.00137 ];
INI_FMASS                 (idx, 1)        =  4.82954E-03 ;
TOT_FMASS                 (idx, 1)        =  4.82954E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.87057E+00 0.00144 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.75525E-01 0.00043 ];
SIX_FF_P                  (idx, [1:   2]) = [  3.44284E-01 0.00197 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.84099E+00 0.00197 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.15618E+00 0.00169 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.15618E+00 0.00169 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.47556E+00 5.8E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02753E+02 6.6E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.15583E+00 0.00176  1.14818E+00 0.00167  8.00086E-03 0.02479 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.15295E+00 0.00094 ];
COL_KEFF                  (idx, [1:   2]) = [  1.15307E+00 0.00170 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.15295E+00 0.00094 ];
ABS_KINF                  (idx, [1:   2]) = [  1.15295E+00 0.00094 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 1.500000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.46836E+01 0.00085 ];
IMP_ALF                   (idx, [1:   2]) = [  1.46732E+01 0.00050 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  6.34535E-06 0.01274 ];
IMP_EALF                  (idx, [1:   2]) = [  6.37904E-06 0.00731 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  3.50584E-01 0.00647 ];
IMP_AFGE                  (idx, [1:   2]) = [  3.50525E-01 0.00333 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  6.40623E-03 0.01527  1.54523E-04 0.10425  9.40422E-04 0.04138  1.01660E-03 0.03708  2.90876E-03 0.02495  1.02450E-03 0.03862  3.61420E-04 0.07122 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  8.86638E-01 0.03929  7.24470E-03 0.08552  3.15587E-02 0.00095  1.10840E-01 0.00134  3.22641E-01 0.00091  1.31443E+00 0.01437  7.77815E+00 0.03916 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  6.87970E-03 0.02700  1.60845E-04 0.15326  1.01751E-03 0.07022  1.18319E-03 0.06895  3.02809E-03 0.03832  1.10170E-03 0.06680  3.88362E-04 0.11894 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  8.79497E-01 0.06373  1.24909E-02 1.0E-05  3.15245E-02 0.00131  1.10905E-01 0.00170  3.23033E-01 0.00135  1.34141E+00 0.00073  8.95363E+00 0.00559 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.48029E-05 0.00369  1.47836E-05 0.00375  1.74272E-05 0.03547 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  1.71046E-05 0.00327  1.70821E-05 0.00331  2.01592E-05 0.03565 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  6.97136E-03 0.02510  1.72033E-04 0.15727  1.04641E-03 0.06171  1.18520E-03 0.05301  3.08189E-03 0.03787  1.09951E-03 0.06140  3.86331E-04 0.11584 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  8.58677E-01 0.06272  1.24909E-02 1.5E-05  3.15414E-02 0.00154  1.10838E-01 0.00176  3.22417E-01 0.00131  1.34079E+00 0.00091  8.90324E+00 0.00713 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.39078E-05 0.02442  1.38968E-05 0.02443  1.34423E-05 0.09600 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.60742E-05 0.02435  1.60614E-05 0.02435  1.55235E-05 0.09571 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  6.34736E-03 0.08988  8.57389E-05 0.51728  8.97438E-04 0.19215  1.05915E-03 0.19309  2.58120E-03 0.12785  1.22194E-03 0.17823  5.01893E-04 0.26284 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  1.12401E+00 0.16920  1.24913E-02 5.9E-05  3.14941E-02 0.00357  1.10564E-01 0.00382  3.22379E-01 0.00351  1.33884E+00 0.00222  8.95229E+00 0.01590 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.62123E-03 0.08955  9.97762E-05 0.52003  9.35225E-04 0.19855  1.11240E-03 0.18921  2.73551E-03 0.12404  1.20005E-03 0.18108  5.38276E-04 0.24883 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  1.10929E+00 0.17375  1.24913E-02 5.9E-05  3.14961E-02 0.00356  1.10578E-01 0.00378  3.22377E-01 0.00343  1.33873E+00 0.00223  8.95229E+00 0.01590 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -4.60971E+02 0.08738 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.48100E-05 0.00243 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  1.71123E-05 0.00159 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.87367E-03 0.01466 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.64290E+02 0.01467 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.47897E-07 0.00213 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  6.52044E-06 0.00170  6.51962E-06 0.00168  6.55557E-06 0.02384 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.32971E-05 0.00245  2.32969E-05 0.00246  2.34670E-05 0.02831 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  3.45126E-01 0.00197  3.44656E-01 0.00199  4.30316E-01 0.03141 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  9.48962E+00 0.03952 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.63979E+01 0.00064  2.86522E+01 0.00110 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  4.81837E+04 0.01784  2.03337E+05 0.00360  4.47427E+05 0.00278  5.07601E+05 0.00197  5.20802E+05 0.00238  7.03235E+05 0.00270  4.78094E+05 0.00148  4.64003E+05 0.00089  3.56893E+05 0.00158  2.88169E+05 0.00243  2.47444E+05 0.00249  2.23544E+05 0.00160  2.02872E+05 0.00163  1.92335E+05 0.00336  1.84987E+05 0.00260  1.56680E+05 0.00284  1.52840E+05 0.00248  1.49564E+05 0.00189  1.44442E+05 0.00454  2.71735E+05 0.00132  2.48646E+05 0.00107  1.69819E+05 0.00403  1.04218E+05 0.00231  1.11451E+05 0.00271  9.74075E+04 0.00333  8.85356E+04 0.00406  1.27727E+05 0.00196  3.00445E+04 0.00505  3.77676E+04 0.00469  3.50069E+04 0.00423  1.97170E+04 0.00836  3.47664E+04 0.00777  2.33128E+04 0.00212  1.89724E+04 0.00277  3.49973E+03 0.02261  3.39552E+03 0.01824  3.53208E+03 0.01070  3.65010E+03 0.01673  3.60758E+03 0.01015  3.59492E+03 0.01857  3.73963E+03 0.00692  3.54738E+03 0.01202  6.66813E+03 0.01108  1.06844E+04 0.01025  1.33684E+04 0.00707  3.47662E+04 0.00646  3.48736E+04 0.00327  3.42533E+04 0.00398  1.99916E+04 0.00599  1.31319E+04 0.00359  9.43179E+03 0.00492  1.01348E+04 0.00644  1.71407E+04 0.00763  2.00902E+04 0.00792  3.31468E+04 0.00394  4.16036E+04 0.00483  5.07250E+04 0.00238  2.80471E+04 0.00385  1.86465E+04 0.00664  1.27119E+04 0.00184  1.08543E+04 0.00462  1.03037E+04 0.00427  8.34630E+03 0.00675  5.38186E+03 0.01150  4.89400E+03 0.00959  4.19312E+03 0.01157  3.43273E+03 0.00758  2.72484E+03 0.01486  1.74574E+03 0.00466  6.25311E+02 0.02822 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.15306E+00 0.00127 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  8.71807E+14 0.00097  4.80974E+13 0.00121 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  3.33027E-01 0.00019  6.37066E-01 0.00074 ];
INF_CAPT                  (idx, [1:   4]) = [  6.25675E-03 0.00115  2.19292E-02 0.00116 ];
INF_ABS                   (idx, [1:   4]) = [  9.16972E-03 0.00090  8.66231E-02 0.00129 ];
INF_FISS                  (idx, [1:   4]) = [  2.91297E-03 0.00086  6.46939E-02 0.00134 ];
INF_NSF                   (idx, [1:   4]) = [  7.34988E-03 0.00087  1.57640E-01 0.00134 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.52315E+00 8.9E-05  2.43670E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03346E+02 8.8E-06  2.02270E+02 8.3E-09 ];
INF_INVV                  (idx, [1:   4]) = [  4.44361E-08 0.00194  2.02331E-06 0.00116 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  3.23870E-01 0.00018  5.50219E-01 0.00065 ];
INF_SCATT1                (idx, [1:   4]) = [  1.08207E-01 0.00068  1.32659E-01 0.00217 ];
INF_SCATT2                (idx, [1:   4]) = [  4.34568E-02 0.00084  3.56738E-02 0.00503 ];
INF_SCATT3                (idx, [1:   4]) = [  4.87751E-03 0.00663  1.12054E-02 0.01860 ];
INF_SCATT4                (idx, [1:   4]) = [ -2.76858E-03 0.01306 -1.26661E-03 0.13858 ];
INF_SCATT5                (idx, [1:   4]) = [  8.57790E-04 0.03584  1.44268E-03 0.07597 ];
INF_SCATT6                (idx, [1:   4]) = [  2.46997E-03 0.00973 -3.91537E-03 0.02112 ];
INF_SCATT7                (idx, [1:   4]) = [  3.79369E-04 0.06048 -5.81465E-04 0.13811 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  3.23901E-01 0.00018  5.50219E-01 0.00065 ];
INF_SCATTP1               (idx, [1:   4]) = [  1.08207E-01 0.00068  1.32659E-01 0.00217 ];
INF_SCATTP2               (idx, [1:   4]) = [  4.34566E-02 0.00084  3.56738E-02 0.00503 ];
INF_SCATTP3               (idx, [1:   4]) = [  4.87728E-03 0.00665  1.12054E-02 0.01860 ];
INF_SCATTP4               (idx, [1:   4]) = [ -2.76852E-03 0.01304 -1.26661E-03 0.13858 ];
INF_SCATTP5               (idx, [1:   4]) = [  8.57833E-04 0.03581  1.44268E-03 0.07597 ];
INF_SCATTP6               (idx, [1:   4]) = [  2.47001E-03 0.00968 -3.91537E-03 0.02112 ];
INF_SCATTP7               (idx, [1:   4]) = [  3.79668E-04 0.06087 -5.81465E-04 0.13811 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.81573E-01 0.00039  4.64473E-01 0.00075 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.83581E+00 0.00039  7.17661E-01 0.00075 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  9.13876E-03 0.00087  8.66231E-02 0.00129 ];
INF_REMXS                 (idx, [1:   4]) = [  1.40679E-02 0.00065  8.90239E-02 0.00187 ];

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

INF_S0                    (idx, [1:   8]) = [  3.18959E-01 0.00018  4.91141E-03 0.00132  2.17741E-03 0.01007  5.48042E-01 0.00063 ];
INF_S1                    (idx, [1:   8]) = [  1.06871E-01 0.00070  1.33589E-03 0.00540  4.32478E-04 0.02868  1.32227E-01 0.00213 ];
INF_S2                    (idx, [1:   8]) = [  4.39069E-02 0.00089 -4.50078E-04 0.01213  2.83930E-04 0.06221  3.53898E-02 0.00495 ];
INF_S3                    (idx, [1:   8]) = [  5.37403E-03 0.00526 -4.96525E-04 0.01112  1.07807E-04 0.19103  1.10976E-02 0.01893 ];
INF_S4                    (idx, [1:   8]) = [ -2.61835E-03 0.01401 -1.50229E-04 0.02842 -5.63036E-06 1.00000 -1.26098E-03 0.14547 ];
INF_S5                    (idx, [1:   8]) = [  8.45232E-04 0.03829  1.25587E-05 0.28422 -5.60970E-05 0.18202  1.49878E-03 0.07320 ];
INF_S6                    (idx, [1:   8]) = [  2.50524E-03 0.00938 -3.52692E-05 0.05801 -5.10437E-05 0.13114 -3.86433E-03 0.02007 ];
INF_S7                    (idx, [1:   8]) = [  4.22442E-04 0.04995 -4.30737E-05 0.07637 -6.25038E-05 0.17282 -5.18961E-04 0.14386 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.18990E-01 0.00018  4.91141E-03 0.00132  2.17741E-03 0.01007  5.48042E-01 0.00063 ];
INF_SP1                   (idx, [1:   8]) = [  1.06871E-01 0.00070  1.33589E-03 0.00540  4.32478E-04 0.02868  1.32227E-01 0.00213 ];
INF_SP2                   (idx, [1:   8]) = [  4.39067E-02 0.00089 -4.50078E-04 0.01213  2.83930E-04 0.06221  3.53898E-02 0.00495 ];
INF_SP3                   (idx, [1:   8]) = [  5.37381E-03 0.00529 -4.96525E-04 0.01112  1.07807E-04 0.19103  1.10976E-02 0.01893 ];
INF_SP4                   (idx, [1:   8]) = [ -2.61829E-03 0.01399 -1.50229E-04 0.02842 -5.63036E-06 1.00000 -1.26098E-03 0.14547 ];
INF_SP5                   (idx, [1:   8]) = [  8.45274E-04 0.03825  1.25587E-05 0.28422 -5.60970E-05 0.18202  1.49878E-03 0.07320 ];
INF_SP6                   (idx, [1:   8]) = [  2.50528E-03 0.00933 -3.52692E-05 0.05801 -5.10437E-05 0.13114 -3.86433E-03 0.02007 ];
INF_SP7                   (idx, [1:   8]) = [  4.22742E-04 0.05032 -4.30737E-05 0.07637 -6.25038E-05 0.17282 -5.18961E-04 0.14386 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.80522E-01 0.00181  4.44568E-01 0.01952 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.81407E-01 0.00260  4.60496E-01 0.02702 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.80932E-01 0.00265  4.41844E-01 0.02712 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.79245E-01 0.00180  4.33943E-01 0.02656 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.84653E+00 0.00181  7.50904E-01 0.01897 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.83754E+00 0.00261  7.25857E-01 0.02551 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.84237E+00 0.00265  7.56592E-01 0.02657 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.85967E+00 0.00180  7.70262E-01 0.02583 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  6.87970E-03 0.02700  1.60845E-04 0.15326  1.01751E-03 0.07022  1.18319E-03 0.06895  3.02809E-03 0.03832  1.10170E-03 0.06680  3.88362E-04 0.11894 ];
LAMBDA                    (idx, [1:  14]) = [  8.79497E-01 0.06373  1.24909E-02 1.0E-05  3.15245E-02 0.00131  1.10905E-01 0.00170  3.23033E-01 0.00135  1.34141E+00 0.00073  8.95363E+00 0.00559 ];

