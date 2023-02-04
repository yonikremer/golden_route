FROM node:14
RUN npm install -g serve

WORKDIR /golden_route/frontend

EXPOSE 3000

CMD serve -s build -l 3000

COPY /frontend/package.json ./
COPY /frontend/package-lock.json ./

RUN npm install

COPY /frontend/public ./public
COPY /frontend/src ./src

RUN npm run build
