# Face Recognition
File di esempio per il riconoscimento facciale con Python.

## Istruzioni per l'esecuzione

**Suggerisco di utilizzare Ubuntu 22.04** se non lo avete installato sul 
vostro pc usate pure una macchina virtuale.

### Installazione su Ubuntu

* Installare Python con i seguenti comandi:
    ```
    sudo apt-get update 
    sudo apt-get install python
    ```
* Scaricare [Miniconda](https://docs.conda.io/en/latest/miniconda.html) ed installarlo 
  con il comando `sh Miniconda3-latest-Linux-x86_64.sh` eventualmente cambiate il nome del file
* Verso la fine dell'installazione verrà chiesto se volete eseguire il **conda init** che di default 
  (se premete invio) non viene eseguito, mentre dovrete scrivere **yes** per eseguirlo **assolutamente**
* Chiudere e riaprire il terminale, ora dovrebbe apparire `(base)` prima del nome del terminale
* Spostarsi nella cartella dov'è presente questo progetto ed eseguire i seguenti comandi:
    ```
    conda create -n cv python
    conda activate cv
    pip install -r requirements.txt
    ```

### Esecuzione del programma
Prima di tutto copiare all'interno di questa cartella (face_recognition) la cartella con le vostre foto
avendo cura di modificare i path nei file prima di eseguirli. Troverete `#FIXME` nelle righe in cui dovrete sostituire
i path.

Per eseguire i file:
* Se si è chiuso il terminale precedente:
  * aprire il terminale
  * spostarsi nella cartella corrente (face_recognition)
  * attivare l'environment con il comando `conda activate cv`
* Altrimenti eseguire il file desiderato con il comando `python simple_detection.py` o `python multi_detection.py`
