#!/usr/bin/bash
#

# Configure nvim
python3 -m pip install --user --upgrade pynvim
nvim +'PlugInstall --sync' +qa
nvim +'UpdateRemotePlugins' +qa
nvim +'CocInstall coc-prettier coc-pairs coc-html coc-yaml coc-neosnippet coc-python' +qa

# Move space theme to nvim themes diretory
cp /home/`whoami`/.config/nvim/space.vim /home/`whoami`/.config/nvim/plugged/vim-airline-themes/autoload/airline/themes/

# Add Plugins for .zshrc
curl -Lo install.sh https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh
sh install.sh --unattended
git clone https://github.com/denysdovhan/spaceship-prompt.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/spaceship-prompt
ln -s ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/spaceship-prompt/spaceship.zsh-theme ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/spaceship.zsh-theme
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# Install Nerd Fonts
font_dir="$HOME/.local/share/fonts"

if [ ! -d "$font_dir" ]
then
    mkdir -p "$font_dir"
fi

cd $font_dir

curl -fLo "Hack Regular Nerd Font Complete Mono.ttf" https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/Hack/Regular/complete/Hack%20Regular%20Nerd%20Font%20Complete%20Mono.ttf
curl -fLo "Hack Regular Nerd Font Complete.ttf" https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/Hack/Regular/complete/Hack%20Regular%20Nerd%20Font%20Complete.ttf

# NPM - Install vtop
cd $HOME
npm install -g vtop
