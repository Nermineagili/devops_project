# Use an Nginx base image
FROM nginx:alpine

# Copy the static files (HTML, CSS, JS) into the Nginx directory
COPY . /usr/share/nginx/html

# Expose port 80 for the frontend
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
