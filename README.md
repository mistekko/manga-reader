# manga-reader

<p>This project is a simple python manga-reader that uses the "viewnior" image viewer (support for others might come in later versions). I'm sure it's not for everyone, but I find it essential to have one that 
<ul>
	<li>Automatically goes to the next folder when a chapter is finished</li>
	<li>Is simpler than soil</li>
	<li>Is CLI-based</li>
</ul>
It's primarily a personal project, so I WILL NOT maintain it regularly, but I do expect to update it occasionally. If you've got a feature request or suggestion for my code (I am very amateur, I expect it to be mediocre), open an issue or pull request and I'll be more than happy to review it when I've got time.</P>

### Installation:

<p>Download <code>manga-reader</code> and run <code>chmod 755 manga-reader</code>. Then, either add the installation directory to your path, move <code>manga-reader</code> to a location on your path, or link it to a location on your path. I like to link it to <code>/bin/mr</code> so that I can change the file without having to use root privileges and execute it without modifying <code>$PATH</code>. However, I'm not sure if this is bad practice, so, er, maybe don't do it simply because I told you to. </p>


### Usage:

manga-reader takes two arguments, one required and one optional:
<ol>
<li>The directory containing the manga</li>
<li>The chapter at which you would like to start, which defaults to 0000 if nothing is provided</li>
</ol>

<p>it will look for chapters based off of a four-digit naming scheme (i.e., 0001, 0231, 0019, etc.), which is a very limited method, but I've yet to generalise it... it ought to work with [mangal](https://github.com/metafates/mangal), which is likely the best manga downloading app on linux at the moment.</p>

<p>Some example uses:</p>
<ul>
<li><code>manga-reader . 12 </code>
	<ul><li>opens chapter 12 of whatever manga exists in your current directory</li>
	</ul></li>
<li><code>manga-reader ~/Documents/books/manga/Usuzumi_No_Hate </code>
<ul><li>starts (opens first chapter of) whatever manga is located in ~/Documents/books/manga/Usuzumi_No_Hate</li>
	</ul></li>
</ul>


### Possible Upcoming Features:

<ul>
	<li>Improve help output</li>
	<li>Support for different image viewers/some way to set image viewer</li>
	<li>Save and resume most recent chapter number</li>
	<li>Better chapter folder selecting</li>
	<li>Going to a previous chapter</li>
	<li>It would be cool if it ran from emacs, but then again, that can be achieved with moderate ease by simply using EXWM</li>
	<li>There needs to be a more normal way to install it</li>
</ul>
