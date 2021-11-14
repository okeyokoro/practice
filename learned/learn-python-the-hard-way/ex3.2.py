from xml.etree.ElementTree import iterparse

f = open('file.xml','w')
doc = """
        <?xml version="1.0"?>
        <buses>
          <bus>
            <id>7574</id>
            <route>147</route>
            <color>#3300ff</color>
            <revenue>true</revenue>
            <direction>North Bound</direction>
            <latitude>41.925682067871094</latitude>
            <longitude>-87.63092803955078</longitude>
            <pattern>2499</pattern>
            <patternDirection>North Bound</patternDirection>
            <run>P675</run>
            <finalStop><![CDATA[Paulina & Howard Terminal]]></finalStop>
            <operator>42493</operator>
          </bus>
          <bus>
            <id>6842</id>
            <route>81</route>
            <color>#996633</color>
            <revenue>true</revenue>
            <direction>East Bound</direction>
            <latitude>41.96847915649414</latitude>
            <longitude>-87.71509087085724</longitude>
            <pattern>1649</pattern>
            <patternDirection>East Bound</patternDirection>
            <run>F259</run>
            <finalStop><![CDATA[Marine Drive & Wilson]]></finalStop>
            <operator>40641</operator>
          </bus>
        </buses>

      """
f.write(doc)
f.close()

def bus_locations (xmlfile):
    parse = iterparse(xmlfile, events = ('bus','bus') )



bus_locations("file.xml")
