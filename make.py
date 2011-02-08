import py_compile
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        py_compile.compile(str(sys.argv[1]))
    elif len(sys.argv) == 3:
        py_compile.compile(str(sys.argv[1]), str(sys.argv[2]))
    else:
        print "Script para compilar arquivos Python para bytecodes .pyo"
        print " "
        print "Dica de Uso:"
        print "1) python make.py arquivo_compilar.py"
        print "2) python make.py arquivo_compilar.py arquivo_saida.pyo"

        sys.exit(2)

