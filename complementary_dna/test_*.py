from complementary_dna import DNA_strand


def test_dna_stand():
    assert DNA_strand("AAAA") == "TTTT"
    assert DNA_strand("ATTGC") == "TAACG"
    assert DNA_strand("GTAT") == "CATA"
