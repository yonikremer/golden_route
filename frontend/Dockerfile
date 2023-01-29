FROM node:14

WORKDIR /golden_route/frontend

COPY /frontend/package.json ./
COPY /frontend/package-lock.json ./
COPY /frontend/public ./public

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
