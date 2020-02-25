# Size of variable arrays:
sizeAlgebraic = 114
sizeStates = 39
sizeConstants = 124
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_algebraic[9] = "I_app in component Protocol (uA_per_uF)"
    legend_voi = "time in component environment (msec)"
    legend_states[0] = "V_m in component membrane_potential (mV)"
    legend_constants[0] = "epi in component parameters (dimensionless)"
    legend_constants[1] = "R in component parameters (joule_per_kelvin_per_kilomole)"
    legend_constants[95] = "Frdy in component parameters (coulomb_per_mole)"
    legend_constants[105] = "Temp in component parameters (kelvin)"
    legend_constants[109] = "FoRT in component parameters (per_mV)"
    legend_constants[2] = "Cmem in component parameters (farad)"
    legend_constants[110] = "Qpow in component parameters (dimensionless)"
    legend_constants[3] = "cellLength in component parameters (um)"
    legend_constants[96] = "cellRadius in component parameters (um)"
    legend_constants[4] = "junctionLength in component parameters (um)"
    legend_constants[97] = "junctionRadius in component parameters (um)"
    legend_constants[5] = "distSLcyto in component parameters (um)"
    legend_constants[6] = "distJuncSL in component parameters (um)"
    legend_constants[7] = "DcaJuncSL in component parameters (cm2_per_sec)"
    legend_constants[8] = "DcaSLcyto in component parameters (cm2_per_sec)"
    legend_constants[9] = "DnaJuncSL in component parameters (cm2_per_sec)"
    legend_constants[10] = "DnaSLcyto in component parameters (cm2_per_sec)"
    legend_constants[106] = "Vcell in component parameters (liter)"
    legend_constants[111] = "Vmyo in component parameters (liter)"
    legend_constants[112] = "Vsr in component parameters (liter)"
    legend_constants[113] = "Vsl in component parameters (liter)"
    legend_constants[114] = "Vjunc in component parameters (liter)"
    legend_constants[107] = "SAjunc in component parameters (um2)"
    legend_constants[108] = "SAsl in component parameters (um2)"
    legend_constants[11] = "J_ca_juncsl in component parameters (liters_per_msec)"
    legend_constants[12] = "J_ca_slmyo in component parameters (liters_per_msec)"
    legend_constants[13] = "J_na_juncsl in component parameters (liters_per_msec)"
    legend_constants[14] = "J_na_slmyo in component parameters (liters_per_msec)"
    legend_constants[15] = "Fjunc in component parameters (dimensionless)"
    legend_constants[98] = "Fsl in component parameters (dimensionless)"
    legend_constants[16] = "Fjunc_CaL in component parameters (dimensionless)"
    legend_constants[99] = "Fsl_CaL in component parameters (dimensionless)"
    legend_constants[115] = "Cli in component parameters (mM)"
    legend_constants[116] = "Clo in component parameters (mM)"
    legend_constants[17] = "Ko in component parameters (mM)"
    legend_constants[18] = "Nao in component parameters (mM)"
    legend_constants[19] = "Cao in component parameters (mM)"
    legend_constants[20] = "Mgi in component parameters (mM)"
    legend_algebraic[22] = "ena_junc in component parameters (mV)"
    legend_algebraic[26] = "ena_sl in component parameters (mV)"
    legend_algebraic[30] = "ek in component parameters (mV)"
    legend_algebraic[32] = "eca_junc in component parameters (mV)"
    legend_algebraic[33] = "eca_sl in component parameters (mV)"
    legend_constants[122] = "ecl in component parameters (mV)"
    legend_constants[21] = "GNa in component parameters (mS_per_uF)"
    legend_constants[22] = "GNaB in component parameters (mS_per_uF)"
    legend_constants[23] = "IbarNaK in component parameters (uA_per_uF)"
    legend_constants[24] = "KmNaip in component parameters (mM)"
    legend_constants[25] = "KmKo in component parameters (mM)"
    legend_constants[26] = "Q10NaK in component parameters (dimensionless)"
    legend_constants[27] = "Q10KmNai in component parameters (dimensionless)"
    legend_constants[28] = "pNaK in component parameters (dimensionless)"
    legend_constants[29] = "gkp in component parameters (mS_per_uF)"
    legend_constants[30] = "GClCa in component parameters (mS_per_uF)"
    legend_constants[31] = "GClB in component parameters (mS_per_uF)"
    legend_constants[32] = "KdClCa in component parameters (mM)"
    legend_constants[33] = "pNa in component parameters (cm_per_sec)"
    legend_constants[34] = "pCa in component parameters (cm_per_sec)"
    legend_constants[35] = "pK in component parameters (cm_per_sec)"
    legend_constants[36] = "Q10CaL in component parameters (dimensionless)"
    legend_constants[37] = "IbarNCX in component parameters (uA_per_uF)"
    legend_constants[38] = "KmCai in component parameters (mM)"
    legend_constants[39] = "KmCao in component parameters (mM)"
    legend_constants[40] = "KmNai in component parameters (mM)"
    legend_constants[41] = "KmNao in component parameters (mM)"
    legend_constants[42] = "ksat in component parameters (dimensionless)"
    legend_constants[43] = "nu in component parameters (dimensionless)"
    legend_constants[44] = "Kdact in component parameters (mM)"
    legend_constants[45] = "Q10NCX in component parameters (dimensionless)"
    legend_constants[46] = "IbarSLCaP in component parameters (uA_per_uF)"
    legend_constants[47] = "KmPCa in component parameters (mM)"
    legend_constants[48] = "GCaB in component parameters (mS_per_uF)"
    legend_constants[49] = "Q10SLCaP in component parameters (dimensionless)"
    legend_constants[50] = "Q10SRCaP in component parameters (dimensionless)"
    legend_constants[51] = "Vmax_SRCaP in component parameters (mM_per_msec)"
    legend_constants[52] = "Kmf in component parameters (mM)"
    legend_constants[53] = "Kmr in component parameters (mM)"
    legend_constants[54] = "hillSRCaP in component parameters (dimensionless)"
    legend_constants[55] = "ks in component parameters (per_msec)"
    legend_constants[56] = "koCa in component parameters (per_mM2_per_msec)"
    legend_constants[57] = "kom in component parameters (per_msec)"
    legend_constants[104] = "kiCa in component parameters (per_mM_per_msec)"
    legend_constants[58] = "kim in component parameters (per_msec)"
    legend_constants[59] = "ec50SR in component parameters (mM)"
    legend_constants[60] = "Bmax_Naj in component parameters (mM)"
    legend_constants[61] = "Bmax_Nasl in component parameters (mM)"
    legend_constants[62] = "koff_na in component parameters (per_msec)"
    legend_constants[63] = "kon_na in component parameters (per_mM_per_msec)"
    legend_constants[64] = "Bmax_TnClow in component parameters (mM)"
    legend_constants[65] = "koff_tncl in component parameters (per_msec)"
    legend_constants[66] = "kon_tncl in component parameters (per_mM_per_msec)"
    legend_constants[67] = "Bmax_TnChigh in component parameters (mM)"
    legend_constants[68] = "koff_tnchca in component parameters (per_msec)"
    legend_constants[69] = "kon_tnchca in component parameters (per_mM_per_msec)"
    legend_constants[70] = "koff_tnchmg in component parameters (per_msec)"
    legend_constants[71] = "kon_tnchmg in component parameters (per_mM_per_msec)"
    legend_constants[72] = "Bmax_CaM in component parameters (mM)"
    legend_constants[73] = "koff_cam in component parameters (per_msec)"
    legend_constants[74] = "kon_cam in component parameters (per_mM_per_msec)"
    legend_constants[75] = "Bmax_myosin in component parameters (mM)"
    legend_constants[76] = "koff_myoca in component parameters (per_msec)"
    legend_constants[77] = "kon_myoca in component parameters (per_mM_per_msec)"
    legend_constants[78] = "koff_myomg in component parameters (per_msec)"
    legend_constants[79] = "kon_myomg in component parameters (per_mM_per_msec)"
    legend_constants[80] = "Bmax_SR in component parameters (mM)"
    legend_constants[81] = "koff_sr in component parameters (per_msec)"
    legend_constants[82] = "kon_sr in component parameters (per_mM_per_msec)"
    legend_constants[117] = "Bmax_SLlowsl in component parameters (mM)"
    legend_constants[118] = "Bmax_SLlowj in component parameters (mM)"
    legend_constants[83] = "koff_sll in component parameters (per_msec)"
    legend_constants[84] = "kon_sll in component parameters (per_mM_per_msec)"
    legend_constants[119] = "Bmax_SLhighsl in component parameters (mM)"
    legend_constants[120] = "Bmax_SLhighj in component parameters (mM)"
    legend_constants[85] = "koff_slh in component parameters (per_msec)"
    legend_constants[86] = "kon_slh in component parameters (per_mM_per_msec)"
    legend_constants[121] = "Bmax_Csqn in component parameters (mM)"
    legend_constants[87] = "koff_csqn in component parameters (per_msec)"
    legend_constants[88] = "kon_csqn in component parameters (per_mM_per_msec)"
    legend_states[1] = "Na_j in component Na_Concentrations (mM)"
    legend_states[2] = "Na_sl in component Na_Concentrations (mM)"
    legend_states[3] = "K_i in component K_Concentration (mM)"
    legend_states[4] = "Ca_j in component Ca_Concentrations (mM)"
    legend_states[5] = "Ca_sl in component Ca_Concentrations (mM)"
    legend_algebraic[0] = "mss in component I_Na (dimensionless)"
    legend_algebraic[11] = "taum in component I_Na (msec)"
    legend_algebraic[1] = "ah in component I_Na (dimensionless)"
    legend_algebraic[12] = "bh in component I_Na (dimensionless)"
    legend_algebraic[24] = "tauh in component I_Na (msec)"
    legend_algebraic[28] = "hss in component I_Na (dimensionless)"
    legend_algebraic[2] = "aj in component I_Na (dimensionless)"
    legend_algebraic[13] = "bj in component I_Na (dimensionless)"
    legend_algebraic[25] = "tauj in component I_Na (msec)"
    legend_algebraic[29] = "jss in component I_Na (dimensionless)"
    legend_states[6] = "m in component I_Na (dimensionless)"
    legend_states[7] = "h in component I_Na (dimensionless)"
    legend_states[8] = "j in component I_Na (dimensionless)"
    legend_algebraic[34] = "I_Na_junc in component I_Na (uA_per_uF)"
    legend_algebraic[35] = "I_Na_sl in component I_Na (uA_per_uF)"
    legend_algebraic[36] = "I_Na in component I_Na (uA_per_uF)"
    legend_algebraic[37] = "I_nabk_junc in component I_NaBK (uA_per_uF)"
    legend_algebraic[38] = "I_nabk_sl in component I_NaBK (uA_per_uF)"
    legend_algebraic[39] = "I_nabk in component I_NaBK (uA_per_uF)"
    legend_constants[100] = "sigma in component I_NaK (dimensionless)"
    legend_algebraic[40] = "fnak in component I_NaK (dimensionless)"
    legend_algebraic[41] = "I_nak_junc in component I_NaK (uA_per_uF)"
    legend_algebraic[42] = "I_nak_sl in component I_NaK (uA_per_uF)"
    legend_algebraic[43] = "I_nak in component I_NaK (uA_per_uF)"
    legend_constants[101] = "gkr in component I_Kr (mS_per_uF)"
    legend_algebraic[3] = "xrss in component I_Kr (dimensionless)"
    legend_algebraic[14] = "tauxr in component I_Kr (msec)"
    legend_states[9] = "x_kr in component I_Kr (dimensionless)"
    legend_algebraic[44] = "rkr in component I_Kr (dimensionless)"
    legend_algebraic[45] = "I_kr in component I_Kr (uA_per_uF)"
    legend_algebraic[46] = "kp_kp in component I_Kp (dimensionless)"
    legend_algebraic[47] = "I_kp_junc in component I_Kp (uA_per_uF)"
    legend_algebraic[48] = "I_kp_sl in component I_Kp (uA_per_uF)"
    legend_algebraic[49] = "I_kp in component I_Kp (uA_per_uF)"
    legend_algebraic[50] = "eks in component I_Ks (mV)"
    legend_constants[89] = "gks_junc in component I_Ks (mS_per_uF)"
    legend_constants[90] = "gks_sl in component I_Ks (mS_per_uF)"
    legend_algebraic[4] = "xsss in component I_Ks (dimensionless)"
    legend_algebraic[15] = "tauxs in component I_Ks (msec)"
    legend_states[10] = "x_ks in component I_Ks (dimensionless)"
    legend_algebraic[51] = "I_ks_junc in component I_Ks (uA_per_uF)"
    legend_algebraic[52] = "I_ks_sl in component I_Ks (uA_per_uF)"
    legend_algebraic[53] = "I_ks in component I_Ks (uA_per_uF)"
    legend_states[11] = "Na_i in component Na_Concentrations (mM)"
    legend_constants[102] = "GtoSlow in component I_to (mS_per_uF)"
    legend_constants[103] = "GtoFast in component I_to (mS_per_uF)"
    legend_algebraic[5] = "xtoss in component I_to (dimensionless)"
    legend_algebraic[6] = "ytoss in component I_to (dimensionless)"
    legend_algebraic[16] = "tauxtos in component I_to (msec)"
    legend_algebraic[17] = "tauytos in component I_to (msec)"
    legend_states[12] = "x_to_s in component I_to (dimensionless)"
    legend_states[13] = "y_to_s in component I_to (dimensionless)"
    legend_algebraic[54] = "I_tos in component I_to (uA_per_uF)"
    legend_algebraic[18] = "tauxtof in component I_to (msec)"
    legend_algebraic[19] = "tauytof in component I_to (msec)"
    legend_states[14] = "x_to_f in component I_to (dimensionless)"
    legend_states[15] = "y_to_f in component I_to (dimensionless)"
    legend_algebraic[55] = "I_tof in component I_to (uA_per_uF)"
    legend_algebraic[56] = "I_to in component I_to (uA_per_uF)"
    legend_algebraic[57] = "aki in component I_Ki (dimensionless)"
    legend_algebraic[58] = "bki in component I_Ki (dimensionless)"
    legend_algebraic[59] = "kiss in component I_Ki (dimensionless)"
    legend_algebraic[60] = "I_ki in component I_Ki (uA_per_uF)"
    legend_algebraic[61] = "I_ClCa_junc in component I_ClCa (uA_per_uF)"
    legend_algebraic[62] = "I_ClCa_sl in component I_ClCa (uA_per_uF)"
    legend_algebraic[63] = "I_ClCa in component I_ClCa (uA_per_uF)"
    legend_algebraic[64] = "I_Clbk in component I_ClCa (uA_per_uF)"
    legend_algebraic[7] = "fss in component I_Ca (dimensionless)"
    legend_algebraic[8] = "dss in component I_Ca (dimensionless)"
    legend_algebraic[20] = "taud in component I_Ca (msec)"
    legend_algebraic[21] = "tauf in component I_Ca (msec)"
    legend_states[16] = "d in component I_Ca (dimensionless)"
    legend_states[17] = "f in component I_Ca (dimensionless)"
    legend_states[18] = "f_Ca_Bj in component I_Ca (dimensionless)"
    legend_states[19] = "f_Ca_Bsl in component I_Ca (dimensionless)"
    legend_constants[91] = "fcaCaMSL in component I_Ca (dimensionless)"
    legend_constants[92] = "fcaCaj in component I_Ca (dimensionless)"
    legend_algebraic[65] = "ibarca_j in component I_Ca (uA_per_uF)"
    legend_algebraic[66] = "ibarca_sl in component I_Ca (uA_per_uF)"
    legend_algebraic[67] = "ibark in component I_Ca (uA_per_uF)"
    legend_algebraic[68] = "ibarna_j in component I_Ca (uA_per_uF)"
    legend_algebraic[69] = "ibarna_sl in component I_Ca (uA_per_uF)"
    legend_algebraic[70] = "I_Ca_junc in component I_Ca (uA_per_uF)"
    legend_algebraic[71] = "I_Ca_sl in component I_Ca (uA_per_uF)"
    legend_algebraic[72] = "I_Ca in component I_Ca (uA_per_uF)"
    legend_algebraic[73] = "I_CaK in component I_Ca (uA_per_uF)"
    legend_algebraic[74] = "I_CaNa_junc in component I_Ca (uA_per_uF)"
    legend_algebraic[75] = "I_CaNa_sl in component I_Ca (uA_per_uF)"
    legend_algebraic[76] = "I_CaNa in component I_Ca (uA_per_uF)"
    legend_algebraic[78] = "I_Catot in component I_Ca (uA_per_uF)"
    legend_algebraic[77] = "Ka_junc in component I_NCX (dimensionless)"
    legend_algebraic[79] = "Ka_sl in component I_NCX (dimensionless)"
    legend_algebraic[80] = "s1_junc in component I_NCX (mM4)"
    legend_algebraic[81] = "s1_sl in component I_NCX (mM4)"
    legend_algebraic[82] = "s2_junc in component I_NCX (mM4)"
    legend_algebraic[83] = "s3_junc in component I_NCX (mM4)"
    legend_algebraic[84] = "s2_sl in component I_NCX (mM4)"
    legend_algebraic[85] = "s3_sl in component I_NCX (mM4)"
    legend_algebraic[86] = "I_ncx_junc in component I_NCX (uA_per_uF)"
    legend_algebraic[87] = "I_ncx_sl in component I_NCX (uA_per_uF)"
    legend_algebraic[89] = "I_ncx in component I_NCX (uA_per_uF)"
    legend_algebraic[90] = "I_pca_junc in component I_PCa (uA_per_uF)"
    legend_algebraic[92] = "I_pca_sl in component I_PCa (uA_per_uF)"
    legend_algebraic[93] = "I_pca in component I_PCa (uA_per_uF)"
    legend_algebraic[94] = "I_cabk_junc in component I_CaBK (uA_per_uF)"
    legend_algebraic[95] = "I_cabk_sl in component I_CaBK (uA_per_uF)"
    legend_algebraic[96] = "I_cabk in component I_CaBK (uA_per_uF)"
    legend_constants[93] = "MaxSR in component SR_Fluxes (dimensionless)"
    legend_constants[94] = "MinSR in component SR_Fluxes (dimensionless)"
    legend_algebraic[10] = "kCaSR in component SR_Fluxes (dimensionless)"
    legend_algebraic[23] = "koSRCa in component SR_Fluxes (per_mM2_per_msec)"
    legend_algebraic[27] = "kiSRCa in component SR_Fluxes (per_mM_per_msec)"
    legend_algebraic[31] = "RI in component SR_Fluxes (mM)"
    legend_states[20] = "Ry_Rr in component SR_Fluxes (mM)"
    legend_states[21] = "Ry_Ro in component SR_Fluxes (mM)"
    legend_states[22] = "Ry_Ri in component SR_Fluxes (mM)"
    legend_algebraic[97] = "J_SRCarel in component SR_Fluxes (mM_per_msec)"
    legend_algebraic[98] = "J_serca in component SR_Fluxes (mM_per_msec)"
    legend_algebraic[99] = "J_SRleak in component SR_Fluxes (mM_per_msec)"
    legend_states[23] = "Ca_sr in component SR_Ca_Concentrations (mM)"
    legend_states[24] = "Ca_i in component Ca_Concentrations (mM)"
    legend_states[25] = "Na_Bj in component Na_Buffers (mM)"
    legend_states[26] = "Na_Bsl in component Na_Buffers (mM)"
    legend_algebraic[101] = "dNa_Bj_dt in component Na_Buffers (mM_per_msec)"
    legend_algebraic[102] = "dNa_Bsl_dt in component Na_Buffers (mM_per_msec)"
    legend_states[27] = "Tn_CL in component Cytosolic_Ca_Buffers (mM)"
    legend_states[28] = "Tn_CHc in component Cytosolic_Ca_Buffers (mM)"
    legend_states[29] = "Tn_CHm in component Cytosolic_Ca_Buffers (mM)"
    legend_states[30] = "CaM in component Cytosolic_Ca_Buffers (mM)"
    legend_states[31] = "Myo_c in component Cytosolic_Ca_Buffers (mM)"
    legend_states[32] = "Myo_m in component Cytosolic_Ca_Buffers (mM)"
    legend_states[33] = "SRB in component Cytosolic_Ca_Buffers (mM)"
    legend_algebraic[100] = "J_CaB_cytosol in component Cytosolic_Ca_Buffers (mM_per_msec)"
    legend_states[34] = "SLL_j in component Junctional_and_SL_Ca_Buffers (mM)"
    legend_states[35] = "SLL_sl in component Junctional_and_SL_Ca_Buffers (mM)"
    legend_states[36] = "SLH_j in component Junctional_and_SL_Ca_Buffers (mM)"
    legend_states[37] = "SLH_sl in component Junctional_and_SL_Ca_Buffers (mM)"
    legend_algebraic[103] = "J_CaB_junction in component Junctional_and_SL_Ca_Buffers (mM_per_msec)"
    legend_algebraic[104] = "J_CaB_sl in component Junctional_and_SL_Ca_Buffers (mM_per_msec)"
    legend_states[38] = "Csqn_b in component SR_Ca_Concentrations (mM)"
    legend_algebraic[105] = "I_Na_tot_junc in component Na_Concentrations (uA_per_uF)"
    legend_algebraic[106] = "I_Na_tot_sl in component Na_Concentrations (uA_per_uF)"
    legend_algebraic[91] = "I_Na_tot_sl2 in component Na_Concentrations (uA_per_uF)"
    legend_algebraic[88] = "I_Na_tot_junc2 in component Na_Concentrations (uA_per_uF)"
    legend_algebraic[107] = "I_K_tot in component K_Concentration (uA_per_uF)"
    legend_algebraic[108] = "I_Ca_tot_junc in component Ca_Concentrations (uA_per_uF)"
    legend_algebraic[109] = "I_Ca_tot_sl in component Ca_Concentrations (uA_per_uF)"
    legend_algebraic[110] = "I_Na_tot in component membrane_potential (uA_per_uF)"
    legend_algebraic[111] = "I_Cl_tot in component membrane_potential (uA_per_uF)"
    legend_algebraic[112] = "I_Ca_tot in component membrane_potential (uA_per_uF)"
    legend_algebraic[113] = "I_tot in component membrane_potential (uA_per_uF)"
    legend_rates[6] = "d/dt m in component I_Na (dimensionless)"
    legend_rates[7] = "d/dt h in component I_Na (dimensionless)"
    legend_rates[8] = "d/dt j in component I_Na (dimensionless)"
    legend_rates[9] = "d/dt x_kr in component I_Kr (dimensionless)"
    legend_rates[10] = "d/dt x_ks in component I_Ks (dimensionless)"
    legend_rates[12] = "d/dt x_to_s in component I_to (dimensionless)"
    legend_rates[13] = "d/dt y_to_s in component I_to (dimensionless)"
    legend_rates[14] = "d/dt x_to_f in component I_to (dimensionless)"
    legend_rates[15] = "d/dt y_to_f in component I_to (dimensionless)"
    legend_rates[16] = "d/dt d in component I_Ca (dimensionless)"
    legend_rates[17] = "d/dt f in component I_Ca (dimensionless)"
    legend_rates[18] = "d/dt f_Ca_Bj in component I_Ca (dimensionless)"
    legend_rates[19] = "d/dt f_Ca_Bsl in component I_Ca (dimensionless)"
    legend_rates[20] = "d/dt Ry_Rr in component SR_Fluxes (mM)"
    legend_rates[21] = "d/dt Ry_Ro in component SR_Fluxes (mM)"
    legend_rates[22] = "d/dt Ry_Ri in component SR_Fluxes (mM)"
    legend_rates[25] = "d/dt Na_Bj in component Na_Buffers (mM)"
    legend_rates[26] = "d/dt Na_Bsl in component Na_Buffers (mM)"
    legend_rates[27] = "d/dt Tn_CL in component Cytosolic_Ca_Buffers (mM)"
    legend_rates[28] = "d/dt Tn_CHc in component Cytosolic_Ca_Buffers (mM)"
    legend_rates[29] = "d/dt Tn_CHm in component Cytosolic_Ca_Buffers (mM)"
    legend_rates[30] = "d/dt CaM in component Cytosolic_Ca_Buffers (mM)"
    legend_rates[31] = "d/dt Myo_c in component Cytosolic_Ca_Buffers (mM)"
    legend_rates[32] = "d/dt Myo_m in component Cytosolic_Ca_Buffers (mM)"
    legend_rates[33] = "d/dt SRB in component Cytosolic_Ca_Buffers (mM)"
    legend_rates[34] = "d/dt SLL_j in component Junctional_and_SL_Ca_Buffers (mM)"
    legend_rates[35] = "d/dt SLL_sl in component Junctional_and_SL_Ca_Buffers (mM)"
    legend_rates[36] = "d/dt SLH_j in component Junctional_and_SL_Ca_Buffers (mM)"
    legend_rates[37] = "d/dt SLH_sl in component Junctional_and_SL_Ca_Buffers (mM)"
    legend_rates[38] = "d/dt Csqn_b in component SR_Ca_Concentrations (mM)"
    legend_rates[23] = "d/dt Ca_sr in component SR_Ca_Concentrations (mM)"
    legend_rates[1] = "d/dt Na_j in component Na_Concentrations (mM)"
    legend_rates[2] = "d/dt Na_sl in component Na_Concentrations (mM)"
    legend_rates[11] = "d/dt Na_i in component Na_Concentrations (mM)"
    legend_rates[3] = "d/dt K_i in component K_Concentration (mM)"
    legend_rates[4] = "d/dt Ca_j in component Ca_Concentrations (mM)"
    legend_rates[5] = "d/dt Ca_sl in component Ca_Concentrations (mM)"
    legend_rates[24] = "d/dt Ca_i in component Ca_Concentrations (mM)"
    legend_rates[0] = "d/dt V_m in component membrane_potential (mV)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -8.09763e1
    states[1] = 9.06
    states[2] = 9.06
    states[3] = 120
    states[4] = 1.737475e-4
    states[5] = 1.031812e-4
    states[6] = 1.405627e-3
    states[7] = 9.867005e-1
    states[8] = 9.91562e-1
    states[9] = 8.641386e-3
    states[10] = 5.412034e-3
    states[11] = 9.06
    states[12] = 4.051574e-3
    states[13] = 9.945511e-1
    states[14] = 4.051574e-3
    states[15] = 9.945511e-1
    states[16] = 7.175662e-6
    states[17] = 1.000681
    states[18] = 2.421991e-2
    states[19] = 1.452605e-2
    states[20] = 8.884332e-1
    states[21] = 8.156628e-7
    states[22] = 1.024274e-7
    states[23] = 0.1e-1
    states[24] = 8.597401e-5
    states[25] = 3.539892
    states[26] = 7.720854e-1
    states[27] = 8.773191e-3
    states[28] = 1.078283e-1
    states[29] = 1.524002e-2
    states[30] = 2.911916e-4
    states[31] = 1.298754e-3
    states[32] = 1.381982e-1
    states[33] = 2.143165e-3
    states[34] = 9.566355e-3
    states[35] = 1.110363e-1
    states[36] = 7.347888e-3
    states[37] = 7.297378e-2
    states[38] = 1.242988
    constants[0] = 1.00000
    constants[1] = 8314.00
    constants[2] = 1.38100e-10
    constants[3] = 100.000
    constants[4] = 0.160000
    constants[5] = 0.450000
    constants[6] = 0.500000
    constants[7] = 1.64000e-06
    constants[8] = 1.22000e-06
    constants[9] = 1.09000e-05
    constants[10] = 1.79000e-05
    constants[11] = 8.24130e-13
    constants[12] = 3.27430e-12
    constants[13] = 1.83130e-14
    constants[14] = 1.63860e-12
    constants[15] = 0.110000
    constants[16] = 0.900000
    constants[17] = 5.40000
    constants[18] = 140.000
    constants[19] = 1.80000
    constants[20] = 1.00000
    constants[21] = 23.0000
    constants[22] = 0.000597000
    constants[23] = 1.00000*1.80000
    constants[24] = 11.0000
    constants[25] = 1.50000
    constants[26] = 1.63000
    constants[27] = 1.39000
    constants[28] = 0.0183300
    constants[29] = 2.00000*0.00100000
    constants[30] = 0.500000*0.109625
    constants[31] = 1.00000*0.00900000
    constants[32] = 0.100000
    constants[33] = 0.500000*1.50000e-08
    constants[34] = 0.500000*0.000540000
    constants[35] = 0.500000*2.70000e-07
    constants[36] = 1.80000
    constants[37] = 1.00000*4.50000
    constants[38] = 0.00359000
    constants[39] = 1.30000
    constants[40] = 12.2900
    constants[41] = 87.5000
    constants[42] = 0.320000
    constants[43] = 0.270000
    constants[44] = 0.000150000
    constants[45] = 1.57000
    constants[46] = 0.0673000
    constants[47] = 0.000500000
    constants[48] = 0.000551300
    constants[49] = 2.35000
    constants[50] = 2.60000
    constants[51] = 0.00531140
    constants[52] = 0.000246000
    constants[53] = 1.70000
    constants[54] = 1.78700
    constants[55] = 25.0000
    constants[56] = 10.0000
    constants[57] = 0.0600000
    constants[58] = 0.00500000
    constants[59] = 0.450000
    constants[60] = 7.56100
    constants[61] = 1.65000
    constants[62] = 0.00100000
    constants[63] = 0.000100000
    constants[64] = 0.0700000
    constants[65] = 0.0196000
    constants[66] = 32.7000
    constants[67] = 0.140000
    constants[68] = 3.20000e-05
    constants[69] = 2.37000
    constants[70] = 0.00333000
    constants[71] = 0.00300000
    constants[72] = 0.0240000
    constants[73] = 0.238000
    constants[74] = 34.0000
    constants[75] = 0.140000
    constants[76] = 0.000460000
    constants[77] = 13.8000
    constants[78] = 5.70000e-05
    constants[79] = 0.0157000
    constants[80] = 19.0000*0.000900000
    constants[81] = 0.0600000
    constants[82] = 100.000
    constants[83] = 1.30000
    constants[84] = 100.000
    constants[85] = 0.0300000
    constants[86] = 100.000
    constants[87] = 65.0000
    constants[88] = 100.000
    constants[89] = 0.00350000
    constants[90] = 0.00350000
    constants[91] = 0.00000
    constants[92] = 0.00000
    constants[93] = 15.0000
    constants[94] = 1.00000
    constants[123] = 0.00000
    constants[95] = 96485.0
    constants[96] = 10.2500
    constants[97] = 0.0150000
    constants[98] = 1.00000-constants[15]
    constants[99] = 1.00000-constants[16]
    constants[100] = (exp(constants[18]/67.3000)-1.00000)/7.00000
    constants[101] = 0.0350000*(power(constants[17]/5.40000, 1.0/2))
    constants[102] = custom_piecewise([equal(constants[0] , 1.00000), 1.00000*0.130000*0.120000 , True, 0.130000*0.300000*0.964000])
    constants[103] = custom_piecewise([equal(constants[0] , 1.00000), 1.00000*0.130000*0.880000 , True, 0.130000*0.300000*0.0360000])
    constants[104] = 0.500000
    constants[105] = 310.000
    constants[106] =  pi*(power(constants[96], 2.00000))*constants[3]*1.00000e-15
    constants[107] = 20150.0* pi*2.00000*constants[4]*constants[97]
    constants[108] =  pi*2.00000*constants[96]*constants[3]
    constants[109] = constants[95]/(constants[1]*constants[105])
    constants[110] = (constants[105]-310.000)/10.0000
    constants[111] = 0.650000*constants[106]
    constants[112] = 0.0350000*constants[106]
    constants[113] = 0.0200000*constants[106]
    constants[114] = 0.0539000*0.0100000*constants[106]
    constants[115] = 15.0000
    constants[116] = 150.000
    constants[117] = (0.0374000*constants[111])/constants[113]
    constants[118] = ((0.00460000*constants[111])/constants[114])*0.100000
    constants[119] = (0.0134000*constants[111])/constants[113]
    constants[120] = ((0.00165000*constants[111])/constants[114])*0.100000
    constants[121] = (0.140000*constants[111])/constants[112]
    constants[122] = (1.00000/constants[109])*log(constants[115]/constants[116])
    return (states, constants)

def computeRates(voi, states, constants): #activation
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[3] = constants[123]
    rates[18] = ((1.70000*states[4])/1.00000)*(1.00000-states[18])-0.0119000*states[18]
    rates[19] = ((1.70000*states[5])/1.00000)*(1.00000-states[19])-0.0119000*states[19]
    rates[27] = constants[66]*states[24]*(constants[64]-states[27])-constants[65]*states[27]
    rates[28] = constants[69]*states[24]*((constants[67]-states[28])-states[29])-constants[68]*states[28]
    rates[29] = constants[71]*constants[20]*((constants[67]-states[28])-states[29])-constants[70]*states[29]
    rates[30] = constants[74]*states[24]*(constants[72]-states[30])-constants[73]*states[30]
    rates[31] = constants[77]*states[24]*((constants[75]-states[31])-states[32])-constants[76]*states[31]
    rates[32] = constants[79]*constants[20]*((constants[75]-states[31])-states[32])-constants[78]*states[32]
    rates[33] = constants[82]*states[24]*(constants[80]-states[33])-constants[81]*states[33]
    rates[34] = constants[84]*states[4]*(constants[118]-states[34])-constants[83]*states[34]
    rates[35] = constants[84]*states[5]*(constants[117]-states[35])-constants[83]*states[35]
    rates[36] = constants[86]*states[4]*(constants[120]-states[36])-constants[85]*states[36]
    rates[37] = constants[86]*states[5]*(constants[119]-states[37])-constants[85]*states[37]
    rates[38] = constants[88]*states[23]*(constants[121]-states[38])-constants[87]*states[38]
    rates[11] = (constants[14]/constants[111])*(states[2]-states[11])
    algebraic[0] = 1.00000/(power(1.00000+exp(-(56.8600+states[0])/9.03000), 2.00000))
    algebraic[11] = 0.129200*exp(-(power((states[0]+45.7900)/15.5400, 2.00000)))+0.0648700*exp(-(power((states[0]-4.82300)/51.1200, 2.00000)))
    rates[6] = (algebraic[0]-states[6])/algebraic[11]
    algebraic[3] = 1.00000/(1.00000+exp(-(states[0]+10.0000)/5.00000))
    algebraic[14] = ((550.000/(1.00000+exp((-22.0000-states[0])/9.00000)))*6.00000)/(1.00000+exp((states[0]--11.0000)/9.00000))+230.000/(1.00000+exp((states[0]--40.0000)/20.0000))
    rates[9] = (algebraic[3]-states[9])/algebraic[14]
    algebraic[4] = 1.00000/(1.00000+exp(-(states[0]+3.80000)/14.2500))
    algebraic[15] = 990.100/(1.00000+exp(-(states[0]+2.43600)/14.1200))
    rates[10] = (algebraic[4]-states[10])/algebraic[15]
    algebraic[5] = 1.00000/(1.00000+exp(-(states[0]-19.0000)/13.0000))
    algebraic[16] = 9.00000/(1.00000+exp((states[0]+3.00000)/15.0000))+0.500000
    rates[12] = (algebraic[5]-states[12])/algebraic[16]
    algebraic[6] = 1.00000/(1.00000+exp((states[0]+19.5000)/5.00000))
    algebraic[17] = 800.000/(1.00000+exp((states[0]+60.0000)/10.0000))+30.0000
    rates[13] = (algebraic[6]-states[13])/algebraic[17]
    algebraic[18] = 8.50000*exp(-(power((states[0]+45.0000)/50.0000, 2.00000)))+0.500000
    rates[14] = (algebraic[5]-states[14])/algebraic[18]
    algebraic[19] = 85.0000*exp(-(power(states[0]+40.0000, 2.00000))/220.000)+7.00000
    rates[15] = (algebraic[6]-states[15])/algebraic[19]
    algebraic[8] = 1.00000/(1.00000+exp(-(states[0]+5.00000)/6.00000))
    algebraic[20] = (1.00000*algebraic[8]*(1.00000-exp(-(states[0]+5.00000)/6.00000)))/(0.0350000*(states[0]+5.00000))
    rates[16] = (algebraic[8]-states[16])/algebraic[20]
    algebraic[7] = 1.00000/(1.00000+exp((states[0]+35.0000)/9.00000))+0.600000/(1.00000+exp((50.0000-states[0])/20.0000))
    algebraic[21] = 1.00000/(0.0197000*exp(-(power(0.0337000*(states[0]+14.5000), 2.00000)))+0.0200000)
    rates[17] = (algebraic[7]-states[17])/algebraic[21]
    algebraic[10] = constants[93]-(constants[93]-constants[94])/(1.00000+power(constants[59]/states[23], 2.50000))
    algebraic[23] = constants[56]/algebraic[10]
    algebraic[27] = constants[104]*algebraic[10]
    rates[21] = (algebraic[23]*(power(states[4], 2.00000))*states[20]-constants[57]*states[21])-(algebraic[27]*states[4]*states[21]-constants[58]*states[22])
    algebraic[1] = custom_piecewise([greater_equal(states[0] , -40.0000), 0.00000 , True, 0.0570000*exp(-(states[0]+80.0000)/6.80000)])
    algebraic[12] = custom_piecewise([greater_equal(states[0] , -40.0000), 0.770000/(0.130000*(1.00000+exp(-(states[0]+10.6600)/11.1000))) , True, 2.70000*exp(0.0790000*states[0])+310000.*exp(0.348500*states[0])])
    algebraic[24] = 1.00000/(algebraic[1]+algebraic[12])
    algebraic[28] = 1.00000/(power(1.00000+exp((states[0]+71.5500)/7.43000), 2.00000))
    rates[7] = (algebraic[28]-states[7])/algebraic[24]
    algebraic[2] = custom_piecewise([greater_equal(states[0] , -40.0000), 0.00000 , True, ((-25428.0*exp(0.244400*states[0])-6.94800e-06*exp(-0.0439100*states[0]))*(states[0]+37.7800))/(1.00000+exp(0.311000*(states[0]+79.2300)))])
    algebraic[13] = custom_piecewise([greater_equal(states[0] , -40.0000), (0.600000*exp(0.0570000*states[0]))/(1.00000+exp(-0.100000*(states[0]+32.0000))) , True, (0.0242400*exp(-0.0105200*states[0]))/(1.00000+exp(-0.137800*(states[0]+40.1400)))])
    algebraic[25] = 1.00000/(algebraic[2]+algebraic[13])
    algebraic[29] = 1.00000/(power(1.00000+exp((states[0]+71.5500)/7.43000), 2.00000))
    rates[8] = (algebraic[29]-states[8])/algebraic[25]
    algebraic[31] = ((1.00000-states[20])-states[21])-states[22]
    rates[20] = (constants[58]*algebraic[31]-algebraic[27]*states[4]*states[20])-(algebraic[23]*(power(states[4], 2.00000))*states[20]-constants[57]*states[21])
    rates[22] = (algebraic[27]*states[4]*states[21]-constants[58]*states[22])-(constants[57]*states[22]-algebraic[23]*(power(states[4], 2.00000))*algebraic[31])
    algebraic[97] = ((constants[55]*states[21])/1.00000)*(states[23]-states[4])
    algebraic[98] = ((power(constants[50], constants[110]))*constants[51]*(power(states[24]/constants[52], constants[54])-power(states[23]/constants[53], constants[54])))/(1.00000+power(states[24]/constants[52], constants[54])+power(states[23]/constants[53], constants[54]))
    algebraic[99] = 5.34800e-06*(states[23]-states[4])
    rates[23] = (algebraic[98]-((algebraic[99]*constants[111])/constants[112]+algebraic[97]))-(constants[88]*states[23]*(constants[121]-states[38])-constants[87]*states[38])
    algebraic[100] = (((((((((((constants[66]*states[24]*(constants[64]-states[27])-constants[65]*states[27])+constants[69]*states[24]*((constants[67]-states[28])-states[29]))-constants[68]*states[28])+constants[71]*constants[20]*((constants[67]-states[28])-states[29]))-constants[70]*states[29])+constants[74]*states[24]*(constants[72]-states[30]))-constants[73]*states[30])+constants[77]*states[24]*((constants[75]-states[31])-states[32]))-constants[76]*states[31])+constants[79]*constants[20]*((constants[75]-states[31])-states[32]))-constants[78]*states[32])+(constants[82]*states[24]*(constants[80]-states[33])-constants[81]*states[33])
    rates[24] = ((-algebraic[98]*constants[112])/constants[111]-algebraic[100])+(constants[12]/constants[111])*(states[5]-states[24])
    algebraic[101] = constants[63]*states[1]*(constants[60]-states[25])-constants[62]*states[25]
    rates[25] = algebraic[101]
    algebraic[102] = constants[63]*states[2]*(constants[61]-states[26])-constants[62]*states[26]
    rates[26] = algebraic[102]
    algebraic[22] = (1.00000/constants[109])*log(constants[18]/states[1])
    algebraic[34] = constants[15]*constants[21]*(power(states[6], 3.00000))*states[7]*states[8]*(states[0]-algebraic[22])
    algebraic[37] = constants[15]*constants[22]*(states[0]-algebraic[22])
    algebraic[40] = 1.00000/(1.00000+0.124500*exp(-0.100000*states[0]*constants[109])+0.0365000*constants[100]*exp(-states[0]*constants[109]))
    algebraic[41] = ((constants[15]*constants[23]*algebraic[40]*constants[17])/(1.00000+power(constants[24]/states[1], 4.00000)))/(constants[17]+constants[25])
    algebraic[68] = (constants[33]*states[0]*constants[95]*constants[109]*(0.750000*states[1]*exp(states[0]*constants[109])-0.750000*constants[18]))/(exp(states[0]*constants[109])-1.00000)
    algebraic[74] = constants[16]*algebraic[68]*states[16]*states[17]*((1.00000-states[18])+constants[92])*(power(constants[36], constants[110]))*0.450000*1.00000
    algebraic[77] = 1.00000/(1.00000+power(constants[44]/states[4], 2.00000))
    algebraic[80] = exp(constants[43]*states[0]*constants[109])*(power(states[1], 3.00000))*constants[19]
    algebraic[82] = exp((constants[43]-1.00000)*states[0]*constants[109])*(power(constants[18], 3.00000))*states[4]
    algebraic[83] = constants[38]*(power(constants[18], 3.00000))*(1.00000+power(states[1]/constants[40], 3.00000))+(power(constants[41], 3.00000))*states[4]*(1.00000+states[4]/constants[38])+constants[39]*(power(states[1], 3.00000))+(power(states[1], 3.00000))*constants[19]+(power(constants[18], 3.00000))*states[4]
    algebraic[86] = ((constants[15]*constants[37]*(power(constants[45], constants[110]))*algebraic[77]*(algebraic[80]-algebraic[82]))/algebraic[83])/(1.00000+constants[42]*exp((constants[43]-1.00000)*states[0]*constants[109]))
    algebraic[105] = algebraic[34]+algebraic[37]+3.00000*algebraic[86]+3.00000*algebraic[41]+algebraic[74]
    rates[1] = ((-algebraic[105]*constants[2])/(constants[114]*constants[95])+(constants[13]/constants[114])*(states[2]-states[1]))-algebraic[101]
    algebraic[26] = (1.00000/constants[109])*log(constants[18]/states[2])
    algebraic[35] = constants[98]*constants[21]*(power(states[6], 3.00000))*states[7]*states[8]*(states[0]-algebraic[26])
    algebraic[38] = constants[98]*constants[22]*(states[0]-algebraic[26])
    algebraic[42] = ((constants[98]*constants[23]*algebraic[40]*constants[17])/(1.00000+power(constants[24]/states[2], 4.00000)))/(constants[17]+constants[25])
    algebraic[69] = (constants[33]*states[0]*constants[95]*constants[109]*(0.750000*states[2]*exp(states[0]*constants[109])-0.750000*constants[18]))/(exp(states[0]*constants[109])-1.00000)
    algebraic[75] = constants[99]*algebraic[69]*states[16]*states[17]*((1.00000-states[19])+constants[91])*(power(constants[36], constants[110]))*0.450000*1.00000
    algebraic[79] = 1.00000/(1.00000+power(constants[44]/states[5], 2.00000))
    algebraic[81] = exp(constants[43]*states[0]*constants[109])*(power(states[2], 3.00000))*constants[19]
    algebraic[84] = exp((constants[43]-1.00000)*states[0]*constants[109])*(power(constants[18], 3.00000))*states[5]
    algebraic[85] = constants[38]*(power(constants[18], 3.00000))*(1.00000+power(states[2]/constants[40], 3.00000))+(power(constants[41], 3.00000))*states[5]*(1.00000+states[5]/constants[38])+constants[39]*(power(states[2], 3.00000))+(power(states[2], 3.00000))*constants[19]+(power(constants[18], 3.00000))*states[5]
    algebraic[87] = ((constants[98]*constants[37]*(power(constants[45], constants[110]))*algebraic[79]*(algebraic[81]-algebraic[84]))/algebraic[85])/(1.00000+constants[42]*exp((constants[43]-1.00000)*states[0]*constants[109]))
    algebraic[106] = algebraic[35]+algebraic[38]+3.00000*algebraic[87]+3.00000*algebraic[42]+algebraic[75]
    rates[2] = ((-algebraic[106]*constants[2])/(constants[113]*constants[95])+(constants[13]/constants[113])*(states[1]-states[2])+(constants[14]/constants[113])*(states[11]-states[2]))-algebraic[102]
    algebraic[103] = (constants[84]*states[4]*(constants[118]-states[34])-constants[83]*states[34])+(constants[86]*states[4]*(constants[120]-states[36])-constants[85]*states[36])
    algebraic[65] = (constants[34]*4.00000*states[0]*constants[95]*constants[109]*(0.341000*states[4]*exp(2.00000*states[0]*constants[109])-0.341000*constants[19]))/(exp(2.00000*states[0]*constants[109])-1.00000)
    algebraic[70] = constants[16]*algebraic[65]*states[16]*states[17]*((1.00000-states[18])+constants[92])*(power(constants[36], constants[110]))*0.450000*1.00000
    algebraic[90] = (constants[15]*(power(constants[49], constants[110]))*constants[46]*(power(states[4], 1.60000)))/(power(constants[47], 1.60000)+power(states[4], 1.60000))
    algebraic[32] = ((1.00000/constants[109])/2.00000)*log(constants[19]/states[4])
    algebraic[94] = constants[15]*constants[48]*(states[0]-algebraic[32])
    algebraic[108] = (algebraic[70]+algebraic[94]+algebraic[90])-2.00000*algebraic[86]
    rates[4] = (((-algebraic[108]*constants[2])/(constants[114]*2.00000*constants[95])+(constants[11]/constants[114])*(states[5]-states[4]))-algebraic[103])+(algebraic[97]*constants[112])/constants[114]+(algebraic[99]*constants[111])/constants[114]
    algebraic[104] = (constants[84]*states[5]*(constants[117]-states[35])-constants[83]*states[35])+(constants[86]*states[5]*(constants[119]-states[37])-constants[85]*states[37])
    algebraic[66] = (constants[34]*4.00000*states[0]*constants[95]*constants[109]*(0.341000*states[5]*exp(2.00000*states[0]*constants[109])-0.341000*constants[19]))/(exp(2.00000*states[0]*constants[109])-1.00000)
    algebraic[71] = constants[99]*algebraic[66]*states[16]*states[17]*((1.00000-states[19])+constants[91])*(power(constants[36], constants[110]))*0.450000*1.00000
    algebraic[92] = (constants[98]*(power(constants[49], constants[110]))*constants[46]*(power(states[5], 1.60000)))/(power(constants[47], 1.60000)+power(states[5], 1.60000))
    algebraic[33] = ((1.00000/constants[109])/2.00000)*log(constants[19]/states[5])
    algebraic[95] = constants[98]*constants[48]*(states[0]-algebraic[33])
    algebraic[109] = (algebraic[71]+algebraic[95]+algebraic[92])-2.00000*algebraic[87]
    rates[5] = ((-algebraic[109]*constants[2])/(constants[113]*2.00000*constants[95])+(constants[11]/constants[113])*(states[4]-states[5])+(constants[12]/constants[113])*(states[24]-states[5]))-algebraic[104]
    algebraic[9] = custom_piecewise([less_equal( voi % 1000.00 , 5.00000), 9.50000 , True, 0.00000])
    #algebraic[9] =activation * -9.5
    algebraic[43] = algebraic[41]+algebraic[42]
    algebraic[30] = (1.00000/constants[109])*log(constants[17]/states[3])
    algebraic[44] = 1.00000/(1.00000+exp((states[0]+74.0000)/24.0000))
    algebraic[45] = constants[101]*states[9]*algebraic[44]*(states[0]-algebraic[30])
    algebraic[46] = 1.00000/(1.00000+exp(7.48800-states[0]/5.98000))
    algebraic[47] = constants[15]*constants[29]*algebraic[46]*(states[0]-algebraic[30])
    algebraic[48] = constants[98]*constants[29]*algebraic[46]*(states[0]-algebraic[30])
    algebraic[49] = algebraic[47]+algebraic[48]
    algebraic[50] = (1.00000/constants[109])*log((constants[17]+constants[28]*constants[18])/(states[3]+constants[28]*states[11]))
    algebraic[51] = constants[15]*constants[89]*(power(states[10], 2.00000))*(states[0]-algebraic[50])
    algebraic[52] = constants[98]*constants[90]*(power(states[10], 2.00000))*(states[0]-algebraic[50])
    algebraic[53] = algebraic[51]+algebraic[52]
    algebraic[54] = constants[102]*states[12]*states[13]*(states[0]-algebraic[30])
    algebraic[55] = constants[103]*states[14]*states[15]*(states[0]-algebraic[30])
    algebraic[56] = algebraic[54]+algebraic[55]
    algebraic[57] = 1.02000/(1.00000+exp(0.238500*((states[0]-algebraic[30])-59.2150)))
    algebraic[58] = (0.491240*exp(0.0803200*((states[0]+5.47600)-algebraic[30]))+exp(0.0617500*((states[0]-algebraic[30])-594.310)))/(1.00000+exp(-0.514300*((states[0]-algebraic[30])+4.75300)))
    algebraic[59] = algebraic[57]/(algebraic[57]+algebraic[58])
    algebraic[60] = 1.00000*0.350000*(power(constants[17]/5.40000, 1.0/2))*algebraic[59]*(states[0]-algebraic[30])
    algebraic[67] = (constants[35]*states[0]*constants[95]*constants[109]*(0.750000*states[3]*exp(states[0]*constants[109])-0.750000*constants[17]))/(exp(states[0]*constants[109])-1.00000)
    algebraic[73] = algebraic[67]*states[16]*states[17]*(constants[16]*(constants[92]+(1.00000-states[18]))+constants[99]*(constants[91]+(1.00000-states[19])))*(power(constants[36], constants[110]))*0.450000*1.00000
    algebraic[107] = ((algebraic[56]+algebraic[45]+algebraic[53]+algebraic[60])-2.00000*algebraic[43])+algebraic[73]+algebraic[49]
    algebraic[110] = algebraic[105]+algebraic[106]
    algebraic[61] = ((constants[15]*constants[30])/(1.00000+constants[32]/states[4]))*(states[0]-constants[122])
    algebraic[62] = ((constants[98]*constants[30])/(1.00000+constants[32]/states[5]))*(states[0]-constants[122])
    algebraic[63] = algebraic[61]+algebraic[62]
    algebraic[64] = constants[31]*(states[0]-constants[122])
    algebraic[111] = algebraic[63]+algebraic[64]
    algebraic[112] = algebraic[108]+algebraic[109]
    algebraic[113] = algebraic[110]+algebraic[111]+algebraic[112]+algebraic[107]
    rates[0] = -(algebraic[113]-algebraic[9])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = 1.00000/(power(1.00000+exp(-(56.8600+states[0])/9.03000), 2.00000))
    algebraic[11] = 0.129200*exp(-(power((states[0]+45.7900)/15.5400, 2.00000)))+0.0648700*exp(-(power((states[0]-4.82300)/51.1200, 2.00000)))
    algebraic[3] = 1.00000/(1.00000+exp(-(states[0]+10.0000)/5.00000))
    algebraic[14] = ((550.000/(1.00000+exp((-22.0000-states[0])/9.00000)))*6.00000)/(1.00000+exp((states[0]--11.0000)/9.00000))+230.000/(1.00000+exp((states[0]--40.0000)/20.0000))
    algebraic[4] = 1.00000/(1.00000+exp(-(states[0]+3.80000)/14.2500))
    algebraic[15] = 990.100/(1.00000+exp(-(states[0]+2.43600)/14.1200))
    algebraic[5] = 1.00000/(1.00000+exp(-(states[0]-19.0000)/13.0000))
    algebraic[16] = 9.00000/(1.00000+exp((states[0]+3.00000)/15.0000))+0.500000
    algebraic[6] = 1.00000/(1.00000+exp((states[0]+19.5000)/5.00000))
    algebraic[17] = 800.000/(1.00000+exp((states[0]+60.0000)/10.0000))+30.0000
    algebraic[18] = 8.50000*exp(-(power((states[0]+45.0000)/50.0000, 2.00000)))+0.500000
    algebraic[19] = 85.0000*exp(-(power(states[0]+40.0000, 2.00000))/220.000)+7.00000
    algebraic[8] = 1.00000/(1.00000+exp(-(states[0]+5.00000)/6.00000))
    algebraic[20] = (1.00000*algebraic[8]*(1.00000-exp(-(states[0]+5.00000)/6.00000)))/(0.0350000*(states[0]+5.00000))
    algebraic[7] = 1.00000/(1.00000+exp((states[0]+35.0000)/9.00000))+0.600000/(1.00000+exp((50.0000-states[0])/20.0000))
    algebraic[21] = 1.00000/(0.0197000*exp(-(power(0.0337000*(states[0]+14.5000), 2.00000)))+0.0200000)
    algebraic[10] = constants[93]-(constants[93]-constants[94])/(1.00000+power(constants[59]/states[23], 2.50000))
    algebraic[23] = constants[56]/algebraic[10]
    algebraic[27] = constants[104]*algebraic[10]
    algebraic[1] = custom_piecewise([greater_equal(states[0] , -40.0000), 0.00000 , True, 0.0570000*exp(-(states[0]+80.0000)/6.80000)])
    algebraic[12] = custom_piecewise([greater_equal(states[0] , -40.0000), 0.770000/(0.130000*(1.00000+exp(-(states[0]+10.6600)/11.1000))) , True, 2.70000*exp(0.0790000*states[0])+310000.*exp(0.348500*states[0])])
    algebraic[24] = 1.00000/(algebraic[1]+algebraic[12])
    algebraic[28] = 1.00000/(power(1.00000+exp((states[0]+71.5500)/7.43000), 2.00000))
    algebraic[2] = custom_piecewise([greater_equal(states[0] , -40.0000), 0.00000 , True, ((-25428.0*exp(0.244400*states[0])-6.94800e-06*exp(-0.0439100*states[0]))*(states[0]+37.7800))/(1.00000+exp(0.311000*(states[0]+79.2300)))])
    algebraic[13] = custom_piecewise([greater_equal(states[0] , -40.0000), (0.600000*exp(0.0570000*states[0]))/(1.00000+exp(-0.100000*(states[0]+32.0000))) , True, (0.0242400*exp(-0.0105200*states[0]))/(1.00000+exp(-0.137800*(states[0]+40.1400)))])
    algebraic[25] = 1.00000/(algebraic[2]+algebraic[13])
    algebraic[29] = 1.00000/(power(1.00000+exp((states[0]+71.5500)/7.43000), 2.00000))
    algebraic[31] = ((1.00000-states[20])-states[21])-states[22]
    algebraic[97] = ((constants[55]*states[21])/1.00000)*(states[23]-states[4])
    algebraic[98] = ((power(constants[50], constants[110]))*constants[51]*(power(states[24]/constants[52], constants[54])-power(states[23]/constants[53], constants[54])))/(1.00000+power(states[24]/constants[52], constants[54])+power(states[23]/constants[53], constants[54]))
    algebraic[99] = 5.34800e-06*(states[23]-states[4])
    algebraic[100] = (((((((((((constants[66]*states[24]*(constants[64]-states[27])-constants[65]*states[27])+constants[69]*states[24]*((constants[67]-states[28])-states[29]))-constants[68]*states[28])+constants[71]*constants[20]*((constants[67]-states[28])-states[29]))-constants[70]*states[29])+constants[74]*states[24]*(constants[72]-states[30]))-constants[73]*states[30])+constants[77]*states[24]*((constants[75]-states[31])-states[32]))-constants[76]*states[31])+constants[79]*constants[20]*((constants[75]-states[31])-states[32]))-constants[78]*states[32])+(constants[82]*states[24]*(constants[80]-states[33])-constants[81]*states[33])
    algebraic[101] = constants[63]*states[1]*(constants[60]-states[25])-constants[62]*states[25]
    algebraic[102] = constants[63]*states[2]*(constants[61]-states[26])-constants[62]*states[26]
    algebraic[22] = (1.00000/constants[109])*log(constants[18]/states[1])
    algebraic[34] = constants[15]*constants[21]*(power(states[6], 3.00000))*states[7]*states[8]*(states[0]-algebraic[22])
    algebraic[37] = constants[15]*constants[22]*(states[0]-algebraic[22])
    algebraic[40] = 1.00000/(1.00000+0.124500*exp(-0.100000*states[0]*constants[109])+0.0365000*constants[100]*exp(-states[0]*constants[109]))
    algebraic[41] = ((constants[15]*constants[23]*algebraic[40]*constants[17])/(1.00000+power(constants[24]/states[1], 4.00000)))/(constants[17]+constants[25])
    algebraic[68] = (constants[33]*states[0]*constants[95]*constants[109]*(0.750000*states[1]*exp(states[0]*constants[109])-0.750000*constants[18]))/(exp(states[0]*constants[109])-1.00000)
    algebraic[74] = constants[16]*algebraic[68]*states[16]*states[17]*((1.00000-states[18])+constants[92])*(power(constants[36], constants[110]))*0.450000*1.00000
    algebraic[77] = 1.00000/(1.00000+power(constants[44]/states[4], 2.00000))
    algebraic[80] = exp(constants[43]*states[0]*constants[109])*(power(states[1], 3.00000))*constants[19]
    algebraic[82] = exp((constants[43]-1.00000)*states[0]*constants[109])*(power(constants[18], 3.00000))*states[4]
    algebraic[83] = constants[38]*(power(constants[18], 3.00000))*(1.00000+power(states[1]/constants[40], 3.00000))+(power(constants[41], 3.00000))*states[4]*(1.00000+states[4]/constants[38])+constants[39]*(power(states[1], 3.00000))+(power(states[1], 3.00000))*constants[19]+(power(constants[18], 3.00000))*states[4]
    algebraic[86] = ((constants[15]*constants[37]*(power(constants[45], constants[110]))*algebraic[77]*(algebraic[80]-algebraic[82]))/algebraic[83])/(1.00000+constants[42]*exp((constants[43]-1.00000)*states[0]*constants[109]))
    algebraic[105] = algebraic[34]+algebraic[37]+3.00000*algebraic[86]+3.00000*algebraic[41]+algebraic[74]
    algebraic[26] = (1.00000/constants[109])*log(constants[18]/states[2])
    algebraic[35] = constants[98]*constants[21]*(power(states[6], 3.00000))*states[7]*states[8]*(states[0]-algebraic[26])
    algebraic[38] = constants[98]*constants[22]*(states[0]-algebraic[26])
    algebraic[42] = ((constants[98]*constants[23]*algebraic[40]*constants[17])/(1.00000+power(constants[24]/states[2], 4.00000)))/(constants[17]+constants[25])
    algebraic[69] = (constants[33]*states[0]*constants[95]*constants[109]*(0.750000*states[2]*exp(states[0]*constants[109])-0.750000*constants[18]))/(exp(states[0]*constants[109])-1.00000)
    algebraic[75] = constants[99]*algebraic[69]*states[16]*states[17]*((1.00000-states[19])+constants[91])*(power(constants[36], constants[110]))*0.450000*1.00000
    algebraic[79] = 1.00000/(1.00000+power(constants[44]/states[5], 2.00000))
    algebraic[81] = exp(constants[43]*states[0]*constants[109])*(power(states[2], 3.00000))*constants[19]
    algebraic[84] = exp((constants[43]-1.00000)*states[0]*constants[109])*(power(constants[18], 3.00000))*states[5]
    algebraic[85] = constants[38]*(power(constants[18], 3.00000))*(1.00000+power(states[2]/constants[40], 3.00000))+(power(constants[41], 3.00000))*states[5]*(1.00000+states[5]/constants[38])+constants[39]*(power(states[2], 3.00000))+(power(states[2], 3.00000))*constants[19]+(power(constants[18], 3.00000))*states[5]
    algebraic[87] = ((constants[98]*constants[37]*(power(constants[45], constants[110]))*algebraic[79]*(algebraic[81]-algebraic[84]))/algebraic[85])/(1.00000+constants[42]*exp((constants[43]-1.00000)*states[0]*constants[109]))
    algebraic[106] = algebraic[35]+algebraic[38]+3.00000*algebraic[87]+3.00000*algebraic[42]+algebraic[75]
    algebraic[103] = (constants[84]*states[4]*(constants[118]-states[34])-constants[83]*states[34])+(constants[86]*states[4]*(constants[120]-states[36])-constants[85]*states[36])
    algebraic[65] = (constants[34]*4.00000*states[0]*constants[95]*constants[109]*(0.341000*states[4]*exp(2.00000*states[0]*constants[109])-0.341000*constants[19]))/(exp(2.00000*states[0]*constants[109])-1.00000)
    algebraic[70] = constants[16]*algebraic[65]*states[16]*states[17]*((1.00000-states[18])+constants[92])*(power(constants[36], constants[110]))*0.450000*1.00000
    algebraic[90] = (constants[15]*(power(constants[49], constants[110]))*constants[46]*(power(states[4], 1.60000)))/(power(constants[47], 1.60000)+power(states[4], 1.60000))
    algebraic[32] = ((1.00000/constants[109])/2.00000)*log(constants[19]/states[4])
    algebraic[94] = constants[15]*constants[48]*(states[0]-algebraic[32])
    algebraic[108] = (algebraic[70]+algebraic[94]+algebraic[90])-2.00000*algebraic[86]
    algebraic[104] = (constants[84]*states[5]*(constants[117]-states[35])-constants[83]*states[35])+(constants[86]*states[5]*(constants[119]-states[37])-constants[85]*states[37])
    algebraic[66] = (constants[34]*4.00000*states[0]*constants[95]*constants[109]*(0.341000*states[5]*exp(2.00000*states[0]*constants[109])-0.341000*constants[19]))/(exp(2.00000*states[0]*constants[109])-1.00000)
    algebraic[71] = constants[99]*algebraic[66]*states[16]*states[17]*((1.00000-states[19])+constants[91])*(power(constants[36], constants[110]))*0.450000*1.00000
    algebraic[92] = (constants[98]*(power(constants[49], constants[110]))*constants[46]*(power(states[5], 1.60000)))/(power(constants[47], 1.60000)+power(states[5], 1.60000))
    algebraic[33] = ((1.00000/constants[109])/2.00000)*log(constants[19]/states[5])
    algebraic[95] = constants[98]*constants[48]*(states[0]-algebraic[33])
    algebraic[109] = (algebraic[71]+algebraic[95]+algebraic[92])-2.00000*algebraic[87]
    algebraic[9] = custom_piecewise([less_equal( voi % 1000.00 , 5.00000), 9.50000 , True, 0.00000])
    algebraic[43] = algebraic[41]+algebraic[42]
    algebraic[30] = (1.00000/constants[109])*log(constants[17]/states[3])
    algebraic[44] = 1.00000/(1.00000+exp((states[0]+74.0000)/24.0000))
    algebraic[45] = constants[101]*states[9]*algebraic[44]*(states[0]-algebraic[30])
    algebraic[46] = 1.00000/(1.00000+exp(7.48800-states[0]/5.98000))
    algebraic[47] = constants[15]*constants[29]*algebraic[46]*(states[0]-algebraic[30])
    algebraic[48] = constants[98]*constants[29]*algebraic[46]*(states[0]-algebraic[30])
    algebraic[49] = algebraic[47]+algebraic[48]
    algebraic[50] = (1.00000/constants[109])*log((constants[17]+constants[28]*constants[18])/(states[3]+constants[28]*states[11]))
    algebraic[51] = constants[15]*constants[89]*(power(states[10], 2.00000))*(states[0]-algebraic[50])
    algebraic[52] = constants[98]*constants[90]*(power(states[10], 2.00000))*(states[0]-algebraic[50])
    algebraic[53] = algebraic[51]+algebraic[52]
    algebraic[54] = constants[102]*states[12]*states[13]*(states[0]-algebraic[30])
    algebraic[55] = constants[103]*states[14]*states[15]*(states[0]-algebraic[30])
    algebraic[56] = algebraic[54]+algebraic[55]
    algebraic[57] = 1.02000/(1.00000+exp(0.238500*((states[0]-algebraic[30])-59.2150)))
    algebraic[58] = (0.491240*exp(0.0803200*((states[0]+5.47600)-algebraic[30]))+exp(0.0617500*((states[0]-algebraic[30])-594.310)))/(1.00000+exp(-0.514300*((states[0]-algebraic[30])+4.75300)))
    algebraic[59] = algebraic[57]/(algebraic[57]+algebraic[58])
    algebraic[60] = 1.00000*0.350000*(power(constants[17]/5.40000, 1.0/2))*algebraic[59]*(states[0]-algebraic[30])
    algebraic[67] = (constants[35]*states[0]*constants[95]*constants[109]*(0.750000*states[3]*exp(states[0]*constants[109])-0.750000*constants[17]))/(exp(states[0]*constants[109])-1.00000)
    algebraic[73] = algebraic[67]*states[16]*states[17]*(constants[16]*(constants[92]+(1.00000-states[18]))+constants[99]*(constants[91]+(1.00000-states[19])))*(power(constants[36], constants[110]))*0.450000*1.00000
    algebraic[107] = ((algebraic[56]+algebraic[45]+algebraic[53]+algebraic[60])-2.00000*algebraic[43])+algebraic[73]+algebraic[49]
    algebraic[110] = algebraic[105]+algebraic[106]
    algebraic[61] = ((constants[15]*constants[30])/(1.00000+constants[32]/states[4]))*(states[0]-constants[122])
    algebraic[62] = ((constants[98]*constants[30])/(1.00000+constants[32]/states[5]))*(states[0]-constants[122])
    algebraic[63] = algebraic[61]+algebraic[62]
    algebraic[64] = constants[31]*(states[0]-constants[122])
    algebraic[111] = algebraic[63]+algebraic[64]
    algebraic[112] = algebraic[108]+algebraic[109]
    algebraic[113] = algebraic[110]+algebraic[111]+algebraic[112]+algebraic[107]
    algebraic[36] = algebraic[34]+algebraic[35]
    algebraic[39] = algebraic[37]+algebraic[38]
    algebraic[72] = algebraic[70]+algebraic[71]
    algebraic[76] = algebraic[74]+algebraic[75]
    algebraic[78] = algebraic[72]+algebraic[73]+algebraic[76]
    algebraic[88] = 3.00000*algebraic[86]+3.00000*algebraic[41]+algebraic[74]
    algebraic[89] = algebraic[86]+algebraic[87]
    algebraic[91] = 3.00000*algebraic[87]+3.00000*algebraic[42]+algebraic[75]
    algebraic[93] = algebraic[90]+algebraic[92]
    algebraic[96] = algebraic[94]+algebraic[95]
    return algebraic

def custom_piecewise(cases):
    """Compute result of a piecewise function"""
    return select(cases[0::2],cases[1::2])

def solve_model():
    """Solve model with ODE solver"""
    from scipy.integrate import ode
    # Initialise constants and state variables
    (init_states, constants) = initConsts()

    # Set timespan to solve over
    voi = linspace(0, 100, 5000)

    # Construct ODE object to solve
    r = ode(computeRates)
    r.set_integrator('vode', method='bdf', atol=1e-06, rtol=1e-06, max_step=1)
    r.set_initial_value(init_states, voi[0])
    r.set_f_params(constants)

    # Solve model
    states = array([[0.0] * len(voi)] * sizeStates)
    states[:,0] = init_states
    for (i,t) in enumerate(voi[1:]):
        if r.successful():
            r.integrate(t)
            states[:,i+1] = r.y
        else:
            break

    # Compute algebraic variables
    algebraic = computeAlgebraic(constants, states, voi)
    return (voi, states, algebraic)

def solve_system():
    from scipy.integrate import ode
    from scipy.integrate import solve_ivp
    import numpy as np
    from functools import partial

    (init_states, constants) = initConsts()

    # Set timespan to solve over
    dt=1
    voi = np.arange(0,5000,dt)

    states = array([[0.0] * len(voi)] * sizeStates)
    states[:,0] = init_states

    for (i,t) in enumerate(voi[1:]):
        if ((i>100)&(i<110)):
            activation = 1.0
        else:
            activation = 0.0
        sol = solve_ivp(partial(computeRates,
                            constants=constants),
                            #activation=activation),
                            voi[i]+[0, dt], states[:,i],
                            method='BDF')


        if (i<(len(voi)-1)):
            states[:,i+1] = sol.y[:,-1]

    #print(init_states)
    #print(sol.y)
    #print('size y=',np.shape(sol.y))
    #print(states)
    #print('size states=',np.shape(states))
    algebraic = computeAlgebraic(constants, states, voi)
    return (voi, states, algebraic)

def plot_model(voi, states, algebraic):
    """Plot variables against variable of integration"""
    import pylab
    (legend_states, legend_algebraic, legend_voi, legend_constants) = createLegends()
    pylab.figure(1)
    pylab.plot(voi,vstack((states,algebraic)).T)
    pylab.xlabel(legend_voi)
#    pylab.legend(legend_states + legend_algebraic, loc='best')
    pylab.show()

def plot_results(voi,states,algebraic):
    "This function is adopted by Hossein.Sharifi"
    (legend_states, legend_algebraic, legend_voi, legend_constants) = createLegends()

    from matplotlib import pyplot as plt
    import matplotlib.gridspec as gridspec
    import numpy as np


    #Ca legends

    #Ca_indicies_for_states=np.array([4,5,23,24,30])
    Ca_indicies_for_states=np.array([23])
    #Ca_indicies_for_algebraic=np.array([46,47])

    size_Ca_for_states=len(Ca_indicies_for_states)
    #size_Ca_for_algebraic=len(Ca_indicies_for_algebraic)

    Ca_legend_states=[""] *size_Ca_for_states
    #Ca_legend_algebraic=[""] *size_Ca_for_algebraic

    Ca_states=array([[0.0] * len(voi)] * size_Ca_for_states)
    #Ca_algebraic=array([[0.0] * len(voi)] * size_Ca_for_algebraic)

    for i in range (0,size_Ca_for_states):
        Ca_legend_states[i]=legend_states[Ca_indicies_for_states[i]]
        Ca_states[i]=states[Ca_indicies_for_states[i]]
    #for i in range (0,size_Ca_for_algebraic):
    #    Ca_legend_algebraic[i]=legend_algebraic[Ca_indicies_for_algebraic[i]]
    #    Ca_algebraic[i]=algebraic[Ca_indicies_for_algebraic[i]]

    #print('size Ca_states=',np.shape(Ca_states))
    #print('size Ca_algebraic=',np.shape(Ca_algebraic))

    #states
    f=plt.figure(1,constrained_layout=True)
    f.set_size_inches([15,6])
    y_axis_states=vstack(Ca_states).T
    plt.plot(voi, y_axis_states)
    plt.xlabel(legend_voi)
    plt.ylabel('Ca_states (milimolar)')
    plt.legend(Ca_legend_states, bbox_to_anchor=(1.05, 1), \
                loc='best', borderaxespad=0.,fontsize='small')

    print("Saving Ca_states figure to")
    save_figure_to_file(f,"Grandi_Ca_states", dpi=None)

    #algebraic
    #f=plt.figure(2,constrained_layout=True)
    #y_axis_algebraic=vstack(Ca_algebraic).T
    #plt.plot(voi, vstack(y_axis_algebraic))
    #plt.xlabel(legend_voi)
    #plt.ylabel('algebraic')
    #plt.legend(Ca_legend_algebraic)
    #print("Saving Ca_algebraic figure to")
    #save_figure_to_file(f, "Ca_algebraic", dpi=None)
    #plt.show()

def save_figure_to_file(f,fname,dpi=None):
    "This function is adopted by Hossein.Sharifi"
    import os
    from skimage.io import imsave

    cwd=os.getcwd()
    filename=cwd + "/"+fname+".png"
    f.savefig(filename, dpi=dpi)

if __name__ == "__main__":
    #(voi, states, algebraic) = solve_model()
    (voi, states, algebraic)=solve_system()
    #plot_model(voi, states, algebraic)
    plot_results(voi, states, algebraic)