### **Current Work**
- [X] Correct Data output from article.py
- [ ] Jinja2 Code, list to Jinja div
- [X] CSS Implemented
- [ ] Heroku Push
- [ ] More formatting [maybe this?](https://help.github.com/articles/basic-writing-and-formatting-syntax/)
- [ ] More comments
- [ ] Clean CSS
- [ ] Sleep

### **Old Reference Site**
#####  [https://elisoncrum.github.io/blog](https://elisoncrum.github.io/blog)

### **README**

> Goal of this program is to make creating blog really simple, mainly for individuals who used to Reddit and Discord markdown.

Turn something like this
````
```h1
more stuff
**bolded stuff**
```
````

into
```html
<h1>more stuff</h1>
<strong>bolded stuff</strong>
``` 

### **Old Program**

> Old Program was created with **JS** and has multiple libraries that are depreciated. The code is also clunky and spaghetti like. Important files are:
> 
> *   [article.js](https://github.com/elisoncrum/blog/blob/master/article.js)
> *   [article example](https://github.com/elisoncrum/blog/blob/master/articles/1.article)

### **New Program**

> So far I have ported the markup engine I created and I need it be rendered by jinja2. The data is correct and needs to be read by jinja. Articles are basically the same, date and title have been changed a bit but the markup is the same.

#### **Why?**

> I decided to use Jinja2 and Flask because it is dynamic and can be used with mySQL and Heroku. The static page was using depreciated libraries.

> *   [article.py](https://github.com/elisoncrum/blog-flask/blob/master/article.py)
> *   [Jinja2](http://jinja.pocoo.org/docs/2.10/)
> *   [Flask](http://flask.pocoo.org/docs/1.0/)
