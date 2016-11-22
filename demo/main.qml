import QtQuick 2.7
import QtQuick.Controls 2.0
import "qml-font-awesome/font_awesome.js" as FontAwesome

ApplicationWindow {
  visible:true;
  FontLoader {
    name: "font_awesome";
    source: "qrc:/fontawesome.ttf";
  }
  Text {
    font.family: "font_awesome"
    font.pointSize: 24
    text: FontAwesome.fa_thumbs_up
  }
}
