## Rodar teste
``` bash
pytest
```

## Remover bilbiotecas (todas)
``` bash
foreach ($package in (pip list --format=freeze | ForEach-Object { $_.Split('=')[0] })) { pip uninstall -y $package }
```

## Instalação dependências
```bash
pip install -r requeriments.txt
```