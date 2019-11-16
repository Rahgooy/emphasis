TextReader = (onload) => {
  dialog = $('<input type="file" />')
  dialog.change((e) => {
    var reader = new FileReader();
    var filename = e.target.files[0].name;
    reader.onload = function(e) {
      var contents = e.target.result;
      onload(contents, filename);
    };
    reader.readAsText(e.target.files[0], "UTF-8");
  });
  dialog.click();
};

DataReader = (onload) => {
  parse = (contents) => {
    var lines = contents.split('\n');
    var data = [];
    var curr = [];
    for (l in lines) {
      if (lines[l] == "") {
        if (curr.length > 0)
          data.push(curr);
        curr = [];
      } else {
        var parts = lines[l].split('\t')
        var winfo = {
          id: parts[0],
          word: parts[1],
          prob: parts.length > 5 ? parseFloat(parts[4]) : parseFloat(parts[2]),
          pos: parts.length > 5 ? parts[5] : "",
          new: false,
          getStyle: function() {
            return this.style + (this.new? ";text-decoration: line-through;": "");
          }
        }
        winfo['style'] = "background-color:rgba(20, 255, 20," + winfo['prob'] + ");";
        curr.push(winfo)
      }
    }
    return data;
  };
  TextReader((contents, filename)=>{
    onload(parse(contents), filename);
  });
};

function validate(gt, data) {
  if (data.length != gt.length)
    return false;

  for (i in data) {
    if (data[i].length != gt[i].length) {
      return false;
    }

    for (j in data[i])
      if (data[i][j].id != gt[i][j].id) {
        return false;
      }
  }
  return true;
}
