#### 1、beautifulsoup使用

1、属性选择

- 1、构建一个soup对象，soup=beautiful('html',lxml)
- 2、选择节点  soup.title
- 3、选择节点文本内容 soup.title.string
- 4、选择节点文本名字 soup.title.name
- 5、选择节点属性 -- 1、所有属性 soup.p.attrs --指定属性 soup.p.attrs['name']
- 6、选择某节点的字节点 soup.p.contents ,soup.p.children返回的是一个生成器
- 7、获取子孙节点 soup.p.descendants,返回的是一个生成器
- 8、获取父节点 soup.p.parent,返回p的直系父节点
- 9、获取所有祖先节点soup.p.parents,
- 10、获取兄弟节点，soup.p.previous_siblings,上一个兄弟节点， soup.p.next_siblings,下一个节点

2、方法选择

- 1、find_all()

  ```python
  1、通过节点名字进行查询
  for ul in soup.find_all(name='ul'):
      print(ul.find_all(name='li'))
  2、通过attrs进行查询
  soup.find_all(attrs={'id':'n1'})
  或者
  soup.find_all(id='n1')
  ```

- find 用法与find_all类似



3、css选择器

- 嵌套选择

  ```python
  for ul in soup.select('ul'):
  	print(ul.select('li'))
  ```

- 获取属性

  ```python
  for li in soup.select('li'):
  	print(li.attrs['id'])
  	print(li['id'])
  ```

- 获取文本

  ```python
  li=soup.select('li')
  print(li.get_text())
  print(li.string)    
  ```

  