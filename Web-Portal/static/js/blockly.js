Blockly.Blocks['Forward'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Move Forward");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip("");
    this.setHelpUrl("");
  }
};

Blockly.Blocks['Back'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Move Backward");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip("");
    this.setHelpUrl("");
  }
};

Blockly.Blocks['Right'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Turn Right");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip("");
    this.setHelpUrl("");
  }
};

Blockly.Blocks['Left'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Turn Left");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip("");
    this.setHelpUrl("");
  }
};

Blockly.Blocks['Loop'] = {
  init: function(){
    this.appendDummyInput()
    .appendField('repeat')
    .appendField(new Blockly.FieldNumber(1, 1, 10), 'loops')
    .appendField("times");
    this.appendStatementInput('DO')
    .appendField('do');
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
  }
};



Blockly.JavaScript['Forward'] = function(block) {
  return 'Forward;\n';
};

Blockly.JavaScript['Back'] = function(block) {
  return 'Back;\n';
};

Blockly.JavaScript['Right'] = function(block) {
  return 'Right;\n';
};

Blockly.JavaScript['Left'] = function(block) {
  return 'Left;\n';
};

Blockly.JavaScript['Loop'] = function(block){
  var stack = Blockly.JavaScript.statementToCode(block, 'DO').split("  ").join("");
  var loop = block.getFieldValue('loops');
  var code = '';
  for(var i=0; i<loop;i++){
    code += stack;
  }
  return code;
}

