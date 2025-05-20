# acr-filename-pattern

Arquivo config.json

```json
{
  "stage": "static",
  "rules": [
    {
      "name": ".*/resources/sql/.*",
      "comment": "Revise o nome do arquivo ${FILE_PATH}",
      "pattern": [
        "*.sql"
      ]
    }
  ]
}
```
