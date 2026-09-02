MTS_MAP = {
    '1': '(n,total)',
    '2': '(n,n₀)',  # elastic scattering
    '5': '(n,anything)',
    '11': '(n,2nd)',  # two neutrons one deuteron
    '16': '(n,2n)',
    '17': '(n,3n)',
    '18': '(n,fission)',
    '19': '(n,f)',  # 1st-chance neutron-induced fission
    '20': '(n,nf)',  # 2nd-chance neutron-induced fission
    '21': '(n,2nf)',  # 3rd-chance neutron-induced fission
    '22': '(n,nα)',  # n,n-alpha
    '23': '(n,n3α)',  # n,n-3alpha
    '24': '(n,2nα)',  # n,2n-alpha
    '25': '(n,3nα)',  # n,3n-alpha
    '28': '(n,np)',
    '29': '(n,n2α)',  # n,n-2alpha
    '30': '(n,2n2α)',  # n,2n-2alpha
    '32': '(n,nd)',
    '33': '(n,nt)',  # n,n-triton
    '34': '(n,n³He)',  # n,n-3He
    '37': '(n,4n)',
    '38': '(n,3nf)',
    '41': '(n,2np)',
    '44': '(n,n2p)',
    '45': '(n,npα)',
    '51': '(n,n₁)',
    '52': '(n,n₂)',
    '53': '(n,n₃)',
    '54': '(n,n₄)',
    '55': '(n,n₅)',
    '56': '(n,n₆)',
    '57': '(n,n₇)',
    '58': '(n,n₈)',
    '59': '(n,n₉)',
    '60': '(n,n₁₀)',
    '61': '(n,n₁₁)',
    '62': '(n,n₁₂)',
    '63': '(n,n₁₃)',
    '64': '(n,n₁₄)',
    '65': '(n,n₁₅)',
    '66': '(n,n₁₆)',
    '67': '(n,n₁₇)',
    '68': '(n,n₁₈)',
    '69': '(n,n₁₉)',
    '70': '(n,n₂₀)',
    '71': '(n,n₂₁)',
    '72': '(n,n₂₂)',
    '73': '(n,n₂₃)',
    '74': '(n,n₂₄)',
    '75': '(n,n₂₅)',
    '76': '(n,n₂₆)',
    '77': '(n,n₂₇)',
    '78': '(n,n₂₈)',
    '79': '(n,n₂₉)',
    '80': '(n,n₃₀)',
    '81': '(n,n₃₁)',
    '82': '(n,n₃₂)',
    '83': '(n,n₃₃)',
    '84': '(n,n₃₄)',
    '85': '(n,n₃₅)',
    '86': '(n,n₃₆)',
    '87': '(n,n₃₇)',
    '88': '(n,n₃₈)',
    '89': '(n,n₃₉)',
    '90': '(n,n₄₀)',
    '91': '(n,nc)',
    '102': '(n,γ)',
    '103': '(n,p)',
    '104': '(n,d)',
    '105': '(n,t)',
    '106': '(n,³He)',
    '107': '(n,α)',
    '108': '(n,2α)',
    '111': '(n,2p)',
    '112': '(n,pα)',
    '115': '(n,pd)',
    '116': '(n,pt)',
    '117': '(n,dα)',
    '452': 'ν-total',
    '455': 'ν-delayed',
    '456': 'ν-prompt',
    '1002': 'S(α,β)',
    '1004': 'S(α,β)',
    '1018': 'χ',  # Unofficial MT for total fission spectrum based on SCALE's convention
}

def decodeMts(zaimt):
    "Tiny helper function to decode the mt label from zaimt"
    zaimt = zaimt.strip()
    mt = zaimt[-5:].lstrip("0") or "0"
    return MTS_MAP.get(mt, "unknown")
