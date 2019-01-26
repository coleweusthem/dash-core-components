# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class SyntaxHighlighter(Component):
    """A SyntaxHighlighter component.
A component for pretty printing code.

Keyword arguments:
- children (string | list; optional): The text to display and highlight
- language (string; optional): the language to highlight code in.
- wrapLines (boolean; optional): a boolean value that determines whether or not each line of code should be wrapped in a parent element. defaults to false, when false one can not take action on an element on the line level. You can see an example of what this enables here
- id (string; optional)
- codeTagProps (dict; optional): props that will be spread into the <code> tag that is the direct parent of the highlighted code elements. Useful for styling/assigning classNames.
- theme (a value equal to: 'light', 'dark'; optional): theme: light or dark
- useInlineStyles (boolean; optional): if this prop is passed in as false, react syntax highlighter will not add style objects to elements, and will instead append classNames. You can then style the code block by using one of the CSS files provided by highlight.js.
- lineNumberContainerStyle (dict; optional): the line numbers container default to appearing to the left with 10px of right padding. You can use this to override those styles.
- lineNumberStyle (dict; optional): inline style to be passed to the span wrapping each number. Can be either an object or a function that recieves current line number as argument and returns style object.
- wrapLines (boolean; optional): a boolean value that determines whether or not each line of code should be wrapped in a parent element. defaults to false, when false one can not take action on an element on the line level. You can see an example of what this enables here
- lineStyle (dict; optional): inline style to be passed to the span wrapping each line if wrapLines is true. Can be either an object or a function that recieves current line number as argument and returns style object."""
    @_explicitize_args
    def __init__(self, children=None, language=Component.UNDEFINED, lineStyle=Component.UNDEFINED, codeTagProps=Component.UNDEFINED, theme=Component.UNDEFINED, useInlineStyles=Component.UNDEFINED, lineNumberContainerStyle=Component.UNDEFINED, lineNumberStyle=Component.UNDEFINED, startingLineNumber=Component.UNDEFINED, wrapLines=Component.UNDEFINED, id=Component.UNDEFINED, showLineNumbers=Component.UNDEFINED, customStyle=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'language', 'wrapLines', 'id', 'codeTagProps', 'theme', 'useInlineStyles', 'lineNumberContainerStyle', 'lineNumberStyle', 'startingLineNumber', 'lineStyle', 'showLineNumbers', 'customStyle']
        self._type = 'SyntaxHighlighter'
        self._namespace = 'dash_core_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'language', 'theme', 'customStyle', 'codeTagProps', 'useInlineStyles', 'showLineNumbers', 'startingLineNumber', 'lineNumberContainerStyle', 'lineNumberStyle', 'wrapLines', 'lineStyle']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(SyntaxHighlighter, self).__init__(children=children, **args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('SyntaxHighlighter(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'SyntaxHighlighter(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
