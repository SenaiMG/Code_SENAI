#O que é um Módulo?
#Considere um módulo como sendo o mesmo que uma biblioteca de código.
#Um arquivo contendo um conjunto de funções que você deseja incluir em seu aplicativo.
#Criar um Módulo
#Para criar um módulo basta salvar o código que você deseja em um arquivo 
# com a extensão de arquivo .py:

#Exemplo
#Salve este código em um arquivo chamado meuModulo.py

#def greeting(name):
#  print("Hello, " + name)

#Usar um módulo
#Agora podemos usar o módulo que acabamos de criar, usando a importinstrução:

import meuModulo

meuModulo.greeting("Jonathan")
#saida Hello, Jonathan

#OBS: Ao usar uma função de um módulo, use a sintaxe: module_name.function_name .


#----------------------------------------------------------------------------------------------
#Variáveis ​​no Módulo
#O módulo pode conter funções, conforme já descrito, 
#mas também variáveis ​​de todos os tipos (arrays, dicionários, objetos etc):

a = meuModulo.person1["age"]
print(a)#saida 36

#-----------------------------------------------------------------------------------------------
#Nomeando um módulo
#Você pode nomear o arquivo do módulo como quiser, mas ele deve ter a extensão de arquivo .py

#Renomear um módulo
#Você pode criar um alias ao importar um módulo, usando a aspalavra-chave:

import mymodule as mx

a = mx.person1["age"]
print(a)#saida 36


#--------------------------------------------------------------------------------------------------
#Módulos embutidos
#Existem vários módulos embutidos no Python, que você pode importar quando quiser.

import platform

x = platform.system()
print(x)#saida windows

#--------------------------------------------------------------------------------------------------
#Usando a função dir()
#Existe uma função interna para listar todos os nomes de funções 
#(ou nomes de variáveis) em um módulo. A dir()função:

x = dir(platform)
print(x)
#saida '_Processor', '_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES',
# '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', 
# '__loader__', '__name__', '__package__', '__spec__', '__version__',
# '_comparable_version', '_component_re', '_default_architecture',
# '_follow_symlinks', '_get_machine_win32', '_ironpython26_sys_version_parser',
# '_ironpython_sys_version_parser', '_java_getprop', '_libc_search', '_mac_ver_xml',
# '_node', '_norm_version', '_os_release_cache', '_os_release_candidates',
# '_os_release_line', '_os_release_unescape', '_parse_os_release', '_platform',
# '_platform_cache', '_pypy_sys_version_parser', '_sys_version', '_sys_version_cache',
# '_sys_version_parser', '_syscmd_file', '_syscmd_ver', '_uname_cache', '_unknown_as_blank',
# '_ver_output', '_ver_stages', 'architecture', 'collections', 'freedesktop_os_release',
# 'functools', 'itertools', 'java_ver', 'libc_ver', 'mac_ver', 'machine', 'node', 'os',
# 'platform', 'processor', 'python_branch', 'python_build', 'python_compiler', 
# 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple',
# 're', 'release', 'subprocess', 'sys', 'system', 'system_alias', 'uname', 'uname_result',
# 'version', 'win32_edition', 'win32_is_iot', 'win32_ver']  

#OBS: A função dir() pode ser usada em todos os módulos, inclusive naqueles que você mesmo criar.

#--------------------------------------------------------------------------------------------------
#Importar do Módulo
#Você pode optar por importar apenas partes de um módulo, usando a palavra- fromchave.

#--------------------------------------------------------------------------------------------------
from mymodule import person1

print (person1["age"])#saida 36

#Observação: ao importar usando a palavra- from chave, 
#não use o nome do módulo ao se referir a elementos no módulo. 
#Exemplo: person1["age"], não mymodule.person1["age"]

#--------------------------------------------------------------------------------------------------
