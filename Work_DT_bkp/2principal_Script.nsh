echo -off

#########################################
#     Definição de variáveis
#########################################
set -v Field_BiosVersion_OK "0620.X.C"
echo "Start.nsh - Field_BiosVersion_OK: %Field_BiosVersion_OK%"
set -v Field_BiosReleaseDate_OK "11/27/2017"
echo "Start.nsh - Field_BiosReleaseDate_OK: %Field_BiosReleaseDate_OK%"
set -v FieldProductName_OK "POS-PIB150DT"
echo "Start.nsh - FieldProductName_OK: %FieldProductName_OK%"

set -v ME_File 0620XC.ROM
echo "Start.nsh - ME_File: %ME_File%"
set -v Command_savemac -savemac
echo "Start.nsh Command_savemac: %Command_savemac%"

color green
set -v ME_Version "11.7.0.3307 H"
echo "Start.nsh - ME_Version: %ME_Version%"
#O parâmetro de comando não foi inserido, pois será executado diretamente.
#Dfinindo a variável Command_TPM_UP, apresenta falhas
set -v TPM_File1 TPM20_7.40.2098.0_to_TPM20_7.62.3126.0.BIN
echo "Start.nsh - TPM_File1: %TPM_File1%"
set -v TPM_File2 TPM20_7.61.2785.0_to_TPM20_7.62.3126.0.BIN
echo "Start.nsh - TPM_File2: %TPM_File2%"

color
set -v Program_BIOS AfuEfi_%ARCH%.efi
echo "Start.nsh - Program_BIOS: %Program_BIOS%"
set -v Program_DMI AMIDEEFI_%ARCH%.efi
echo "Start.nsh - Program_DMI: %Program_DMI%"
set -v Program_Update_ME fpt_%ARCH%.efi
echo "Start.nsh - Program_Update_ME: %Program_Update_ME%"
set -v Program_Update_TPM TPMFactoryUpd_%ARCH%.efi
echo "Start.nsh - Program_Update_TPM: %Program_Update_TPM%"
set -v Program_Info_ME MEInfo_%ARCH%.efi
echo "Start.nsh - Program_Info_ME: %Program_Info_ME%"
set -v Program_ME_Manuf MEManuf_%ARCH%.efi
echo "Start.nsh - Program_ME_Manuf: %Program_ME_Manuf%"
set -v Command_Closemnf "%Program_Update_ME% -closemnf -Y"
echo "Start.nsh - Command_Closemnf: %Command_Closemnf%"
set -v Command_EOL "%Program_ME_Manuf% -eol"
echo "Start.nsh - Command_EOL: %Command_EOL%"
set -v Command_MEManuf "%Program_ME_Manuf%"
echo "Start.nsh - Command_MEManuf: %Command_MEManuf%"
set -v Command_Update_ME "%Program_Update_ME% -f %ME_File% -savemac"
echo "Start.nsh - Command_Update_ME: %Command_Update_ME%"
set -v Command_UUID "%Program_DMI% /su"
echo "Start.nsh - Command_UUID: %Command_UUID%"
set -v Command_Type1_NS "%Program_DMI% /ss"
echo "Start.nsh - Command_Type1_NS: %Command_Type1_NS%"
set -v Command_Type2_NS "%Program_DMI% /bs"
echo "Start.nsh - Command_Type2_NS: %Command_Type2_NS%"
set -v Command_Type3_NS "%Program_DMI% /cs"
echo "Start.nsh - Command_Type3_NS: %Command_Type3_NS%"
set -v Command_Type3_CA "%Program_DMI% /ca"
echo "Start.nsh - Command_Type3_CA: %Command_Type3_CA%"
set -v Command_Type4_SF "%Program_DMI% /SF %FieldProductName_OK%"
echo "Start.nsh - Command_Type4_SF: %Command_Type4_SF%"
set -v TAGNUMPATRIMONIO "NULL"
echo "Start.nsh - TAGNUMPATRIMONIO: %TAGNUMPATRIMONIO%"

#########################################
#     Salva NS Placa-Mãe (DMI Type 2)
#########################################
SalvaNS_Type2.nsh
if "%NS_PLM_TYPE_2%" ne "" then
	color yellow
	echo "Start.nsh - NS da PLM (Type2): %NS_PLM_TYPE_2%"
	color
endif
#NÃ£o repete etapas dos testes finais - melhoria
if "%PULA_ETAPA%" ne "" then
	goto %PULA_ETAPA%
endif

#########################################
#           Verifica ME
#########################################
# Verifica primeiramente se o ME está correto,
# se não estiver grava sem nem pedir o MENU!
ME.nsh
if %lasterror% ne 0 then
	exit %lasterror%
endif

#########################################
#                    MENU
#########################################
# Menu irá setar a variável %op_escolha% com a opção escolhida
:Menu
Menu.nsh
goto %op_escolha%

#########################################
#               PASSO1
#########################################
:Passo1
Passo1.nsh
if %lasterror% ne 0 then
	exit %lasterror%
endif
#Removido save Passo2

#########################################
#               PASSO2
#########################################
:Passo2
Passo2.nsh
if %lasterror% ne 0 then
	exit %lasterror%
endif

#########################################
#           TESTES FINAIS
#########################################
:TestesFinais
TestesFinais.nsh
if %lasterror% ne 0 then
	exit %lasterror%
endif

#########################################
#            FIM
#########################################
Sucesso.nsh