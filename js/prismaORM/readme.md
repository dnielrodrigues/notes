# Basics
``` bash
# Start prisma
$ npx prisma init

# Reverse engineering to a existing database
mkdir -p prisma/migrations/0_init
npx prisma migrate diff \
--from-empty \
--to-schema-datamodel prisma/schema.prisma \
--script > prisma/migrations/0_init/migration.sql
npx prisma migrate resolve --applied 0_init
npx prisma migrate deploy
npx prisma db pull
npx prisma format
npx prisma generate
```
