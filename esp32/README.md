# Scripts rechstreeks vanuit VSCode draaien op je device

De standaard MicroPython plugin werkt niet op Windows. Maar er is wel een andere manier.

Installeer het package ampy:
```
pip install ampy
```

Zet het bestandje tasks.json met de volgende inhoud in een mapje .vscode in werkfolder (pas zelf de COM poort aan en evt Baud rate)
```json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "ampy",
            "type": "shell",
            "command": "ampy -b 115200 -p COM7 -d 1 run ${file} --no-output",
            "group": {
                "kind": "build",
                "isDefault": true
            }
        }
    ]
}
```

Met `Ctrl + Shift + B` kun je vervolgens het py-script dat open staat op je device runnen.
