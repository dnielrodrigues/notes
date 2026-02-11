Start prisma: `npx prisma init`  

Put this on ./prisma/schema.prisma:  
```prisma
generator client {
  provider        = "prisma-client-js"
  previewFeatures = ["relationJoins"]
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

```

Create schema.prisma from source: `npx prisma db pull`  

Create initial migration and apply it:  
```bash
mkdir -p prisma/migrations/0_init
npx prisma migrate diff \
--from-empty \
--to-schema-datamodel prisma/schema.prisma \
--script > prisma/migrations/0_init/migration.sql
npx prisma migrate resolve --applied 0_init
```

Generate prisma client: `npx prisma generate`  
