def main(str):
    str = str.replace("\n", "")
    str = str.replace(" ", "")
    str = str.replace("'", "")
    spis0 = str.split(",")
    dict = {}
    for str in spis0[:len(spis0)-1:]:
        fi = str.find("(")
        se = str.find(")")
        str2 = str[fi+1:se:]
        str2 = str2.replace("'", "")
        spis = str2.split('.')

        fi = str.find("\"")
        se = str.find("\".")

        str2 = str[fi+1:se:]
        dict[str2] = spis
    return dict

print(main('do [declare list(\'erce_26\'. \'ledixe\')==> "inin". ], [ declare list(\n\'diatri_659\' . \'antege\'.\'esar\' . \'maqu_883\' ) ==> "soedza_849". ],[\ndeclare list( \'zara\' . \'rier\' . \'ardixe_787\' . \'veus_49\' ) ==>\n"tige_832".],od'))
#print(main("""do[ declare list('diatari_105' . 'insote_564' ) ==> "enen". ], [declare list( 'edenen' .'dianqu' . 'leeser_273'. 'anan_772' ) ==>"usreon". ],[declare list('tibeor' . 'bealari' . 'esle' ) ==>"esedso". ], od"""))