# Melhor Forma de Criar uma Nova Tabela no Next.js com Prisma

A maneira mais eficiente e segura de criar uma nova tabela em um projeto Next.js usando Prisma como ORM é através do sistema de migrações. Aqui está o fluxo completo:

## Fluxo Recomendado

1. **Edite o schema.prisma**  
   Adicione seu novo modelo no arquivo `prisma/schema.prisma`:

   ```prisma
   model Product {
     id          Int      @id @default(autoincrement())
     name        String
     price       Decimal  @db.Decimal(10, 2)
     description String?
     createdAt   DateTime @default(now())
     updatedAt   DateTime @updatedAt
   }
   ```

2. **Crie e aplique a migração**  
   Execute o comando interativo:

   ```bash
   npx prisma migrate dev --name add_product_table
   ```

   Isso vai:
   - Gerar um arquivo SQL de migração
   - Aplicar as alterações no banco de dados
   - Atualizar automaticamente o cliente Prisma

## Boas Práticas Adicionais

1. **Para alterações em produção**:
   ```bash
   npx prisma migrate deploy
   ```

2. **Verifique o histórico de migrações**:
   ```bash
   npx prisma migrate status
   ```

3. **Para resetar o banco em desenvolvimento** (cuidado!):
   ```bash
   npx prisma migrate reset
   ```

## Fluxo Alternativo (para prototipação rápida)

Se estiver em desenvolvimento inicial e não precisar de versionamento:

```bash
npx prisma db push
```

Isso sincroniza o schema diretamente com o banco sem criar migrações, mas não é recomendado para projetos em produção.

## Dicas Importantes

- Sempre revise os arquivos de migração gerados em `prisma/migrations`
- Considere usar `npx prisma studio` para visualizar os dados
- Para projetos TypeScript, execute `npx prisma generate` após alterações

Este método garante que todas as alterações no banco de dados sejam rastreáveis e possam ser revertidas se necessário.
