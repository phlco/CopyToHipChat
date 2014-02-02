# Copy To HipChat
Sublime Plugin to append `/code` to a selection of text for syntax highlighting in HipChat.

# Usage
Select text and press `shift+command+h`. Paste into HipChat.

By default the file name and path are appended as a comment at the message. These settings can be changed by altering the JSON in `copy_to_hipchat.sublime-settings`

## Output
```ruby
# optional/path/to/filename.rb
class Animal
end
```
```js
// optional_filename.js
function Animal(){
}
```

## Installation
### Package Control
You can install directly from Package Control. First install [Package Control](https://sublime.wbond.net/) then search for Copy To HipChat.

### Manually
Clone this repo into your Packages Directory `~/Library/Application Support/Sublime Text 3/Packages`

# Resources
- [HipChat Slash Commands](http://help.hipchat.com/knowledgebase/articles/64451-work-faster-with-slash-commands)
- [Sublime Text 3 API Docs](https://www.sublimetext.com/docs/3/api_reference.html)
