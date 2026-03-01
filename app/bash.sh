#!/bin/bash

#
# Função de exemplo que retorna um trecho da biblia
#
# bible() {
#   script="/home/plotzky/PycharmProjects/Python/pythonProject/run_terminal.py"
#   python "$script" "$@"
# }
#

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Verifica se a função já está  no .bashrc
if ! grep -qF "bible() {" ~/.bashrc; then

    script="$script_dir/main.py"

    # Adiciona função bible ao final do .bashrc
    echo -e "\nbible() {\n  python \"$script\"\n}" >> ~/.bashrc

    # Atualize o .bashrc
    source ~/.bashrc
fi


