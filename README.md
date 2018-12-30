<h3><strong>README</strong></h3>
<blockquote>
<p>Goal of this program is to make creating blog really simple, mainly for individuals who used to Reddit and Discord markdown.</p>
</blockquote>
<p>Turn something like this</p>
<pre><code>`<span class="javascript"></span>``<span class="javascript">h1
more stuff
**bolded stuff**
</span>``<span class="javascript"></span>`
</code></pre>
<p>into</p>
<pre><code><span class="hljs-tag">&lt;<span class="hljs-title">h1</span>&gt;</span>more stuff<span class="hljs-tag">&lt;/<span class="hljs-title">h1</span>&gt;</span>
<span class="hljs-tag">&lt;<span class="hljs-title">strong</span>&gt;</span>bolded stuff<span class="hljs-tag">&lt;/<span class="hljs-title">strong</span>&gt;</span>
</code></pre>
<h3><strong>Old Program</strong></h3>
<blockquote>
<p>Old Program was created with <strong>JS</strong> and has multiple libraries that are depreciated. The code is also clunky and spaghetti like. Important files are:</p>
<ul>
<li><a href="https://github.com/elisoncrum/blog/blob/master/article.js">article.js</a></li>
<li><a href="https://github.com/elisoncrum/blog/blob/master/articles/1.article">article example</a></li>
</ul>
</blockquote>
<h3><strong>New Program</strong></h3>
<blockquote>
<p>So far I have ported the markup engine I created and I need it be rendered by jinja2. The data is correct and needs to be read by jinja. Articles are basically the same, date and title have been changed a bit but the markup is the same.</p>
</blockquote>
<h4><strong>Why?</strong></h4>
<blockquote>
<p>I decided to use Jinja2 and Flask because it is dynamic and can be used with mySQL and Heroku. The static page was using depreciated libraries.</p>
</blockquote>
<blockquote>
<ul>
<li><a href="https://github.com/elisoncrum/blog-flask/blob/master/article.py">article.py</a></li>
<li><a href="http://jinja.pocoo.org/docs/2.10/">Jinja2</a></li>
<li><a href="http://flask.pocoo.org/docs/1.0/">Flask</a></li>
</ul>
</blockquote>
