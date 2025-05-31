# Reverse engineering
```
rm -rf node_modules prisma
npm install
npx prisma init
npx prisma db pull
npx prisma generate # PS: fix the relation bugs (BigInt)
mkdir -p prisma/migrations/0_init
npx prisma migrate diff \
--from-empty \
--to-schema-datamodel prisma/schema.prisma \
--script > prisma/migrations/0_init/migration.sql
```
