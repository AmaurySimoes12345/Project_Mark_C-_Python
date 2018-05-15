echo -off
echo "UP_TPM.nsh - Capturando versao do TPM para atualizar."
# Chamada para verificar o TPM é aqui
color blue
#%Program_Update_TPM% -info > Version.log - Já foi gerado no ME.nsh
type -u Version.log | find "7.40.2098.0"
if %lasterror% eq 0 then
	color green
	echo "UP_TPM.nsh - Vou atualizar para a versao:7.62.3126.0 - Atualizar com arquivo 1"
	color
	#Não executo com as a variável de Comando porque apresentou erro
	#%Command_Update_TPM1%
	%Program_Update_TPM% -update tpm20-emptyplatformauth -firmware %TPM_File1%
	#set TPM_UP 1
	if %lasterror% ne 0 then
		#set -d TPM_UP
		color red
		echo "UP_TPM.nsh - ERRO!"
		Erro.nsh
	endif
else
	color yellow
	echo "UP_TPM.nsh - Esta maquina esta com a versao 7.61.2785.0"
	echo "UP_TPM.nsh - Vou atualizar para a versao:7.62.3126.0 - Atualizar com arquivo 2"
	color
	#Não executo com as a variável de Comando porque apresentou erro
	#%Command_Update_TPM2%
	%Program_Update_TPM% -update tpm20-emptyplatformauth -firmware %TPM_File2%
	#set TPM_UP 1
	if %lasterror% ne 0 then
		#set -d TPM_UP
		color red
		echo "UP_TPM.nsh - ERRO!"
		Erro.nsh
	endif
	#Remivod daqui o Salva etapa
	Desliga.nsh
endif
:END