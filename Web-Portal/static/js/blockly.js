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
        .appendField("Move Right");
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
        .appendField("Move Left");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
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

