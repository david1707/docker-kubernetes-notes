# Use node image
FROM node:14

# Set up this as your working directory (every command will run here)
WORKDIR /app

# Copy everything inside the '/app' directory
COPY . /app

# Run "npm install" inside /app
RUN npm install

# Documents that you have to expose this port (you still have to run -p 80:80)
EXPOSE 80

# RUN are executed when the image is created, CMD when a container is started
CMD ["node", "server.js"]
