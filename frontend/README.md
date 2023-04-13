# vue-frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```


## Publish to Github pages after build
```
git add dist -f
git commit -m "adding dist"
cd ..
git subtree push --prefix frontend/dist origin gh-pages
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
