function youtube()
{
    if [[ -f .okay_y ]]; then
        echo ""

    else
        pkg install -y curl &> /dev/null
        pkg install -y ffmpeg &> /dev/null
        [[ -d ~/storage ]] || termux-setup-storage
        curl -L https://yt-dl.org/downloads/latest/youtube-dl -o ${path_bin}youtube-dl &> /dev/null
        chmod a+rx /data/data/com.termux/files/usr/bin/youtube-dl
        > .okay_y
    fi

    clear
    printf "\e[1;34m
 1) MP3/MUSICA
 2) MP4/VIDEO

 ===> \e[1;36m"
    read option
    printf "\e[1;34m URL PARA O DOWNLAOD: \e[1;36m"
    read url

    if [[ ${option} -eq 1 ]]; then
        printf "\e[1;34m Fazendo o download MP3\e[1;36m\n"
        youtube-dl --extract-audio --audio-format mp3 $url | sed 's/\[/\ [/g;s/\[K/\ [/g;s/Deleting/\ Deleting/g'
        [[ $? -eq 0 ]] && printf "\e[1;34mSucesso!\n"

    else
        printf "\e[1;34m Fazendo o download MP4\e[1;36m"
        youtube-dl ${url}
        [[ $? -eq 0 ]] && printf "\e[1;34m Sucesso!"
    fi
}
youtube
