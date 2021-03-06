<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="2.18.14" simplifyAlgorithm="0" minimumScale="0" maximumScale="1e+08" simplifyDrawingHints="1" minLabelScale="0" maxLabelScale="1e+08" simplifyDrawingTol="1" readOnly="1" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" scaleBasedLabelVisibilityFlag="0">
  <edittypes>
    <edittype widgetv2type="TextEdit" name="id">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="upi">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="use">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="plot_numbe">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="area">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="scheme_id">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="crs_id">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="scheme_fie">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
  </edittypes>
  <renderer-v2 forceraster="0" symbollevels="0" type="singleSymbol" enableorderby="0">
    <symbols>
      <symbol alpha="1" clip_to_extent="1" type="fill" name="0">
        <layer pass="0" class="SimpleFill" locked="0">
          <prop k="border_width_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="color" v="255,255,0,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
        </layer>
        <layer pass="0" class="GeometryGenerator" locked="0">
          <prop k="SymbolType" v="Marker"/>
          <prop k="geometryModifier" v="nodes_to_points($geometry)"/>
          <symbol alpha="1" clip_to_extent="1" type="marker" name="@0@1">
            <layer pass="0" class="GeometryGenerator" locked="0">
              <prop k="SymbolType" v="Line"/>
              <prop k="geometryModifier" v="make_line( point_n( $geometry,(@geometry_part_num)),point_n( $geometry,(@geometry_part_num+1)))"/>
              <symbol alpha="1" clip_to_extent="1" type="line" name="@@0@1@0">
                <layer pass="0" class="MarkerLine" locked="0">
                  <prop k="interval" v="3"/>
                  <prop k="interval_map_unit_scale" v="0,0,0,0,0,0"/>
                  <prop k="interval_unit" v="MM"/>
                  <prop k="offset" v="2"/>
                  <prop k="offset_along_line" v="0"/>
                  <prop k="offset_along_line_map_unit_scale" v="0,0,0,0,0,0"/>
                  <prop k="offset_along_line_unit" v="MM"/>
                  <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="placement" v="centralpoint"/>
                  <prop k="rotate" v="1"/>
                  <symbol alpha="1" clip_to_extent="1" type="marker" name="@@@0@1@0@0">
                    <layer pass="0" class="FontMarker" locked="0">
                      <prop k="angle" v="0"/>
                      <prop k="angle_dd_active" v="1"/>
                      <prop k="angle_dd_expression" v="CASE WHEN degrees(&#xd;&#xa;&#x9;azimuth(point_n($geometry, @geometry_part_num), point_n($geometry, @geometry_part_num+1))&#xd;&#xa;&#x9;) > 180 AND degrees(&#xd;&#xa;&#x9;azimuth(point_n($geometry, @geometry_part_num), point_n($geometry, @geometry_part_num+1))&#xd;&#xa;&#x9;) &lt; 360&#xd;&#xa;&#x9;THEN line_interpolate_angle( $geometry, 0) + 90&#xd;&#xa;ELSE&#xd;&#xa;&#x9;line_interpolate_angle( $geometry, 0) + 270&#xd;&#xa;END"/>
                      <prop k="angle_dd_field" v=""/>
                      <prop k="angle_dd_useexpr" v="1"/>
                      <prop k="char_dd_active" v="1"/>
                      <prop k="char_dd_expression" v="format_number(&#xd;&#xa;&#x9;length(make_line(&#xd;&#xa;&#x9;transform(point_n($geometry,(@geometry_part_num)), 'EPSG:4326',  @flts_source_crs ),&#xd;&#xa;&#x9;transform(point_n( $geometry,(@geometry_part_num+1)), 'EPSG:4326',  @flts_source_crs )&#xd;&#xa;&#x9;)),&#xd;&#xa;&#x9;2&#xd;&#xa;) ||' m'"/>
                      <prop k="char_dd_field" v=""/>
                      <prop k="char_dd_useexpr" v="1"/>
                      <prop k="chr" v="A"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="font" v="Arial"/>
                      <prop k="horizontal_anchor_point" v="1"/>
                      <prop k="joinstyle" v="bevel"/>
                      <prop k="offset" v="0,0"/>
                      <prop k="offset_dd_active" v="0"/>
                      <prop k="offset_dd_expression" v=""/>
                      <prop k="offset_dd_field" v=""/>
                      <prop k="offset_dd_useexpr" v="0"/>
                      <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="outline_color" v="0,0,0,255"/>
                      <prop k="outline_width" v="0"/>
                      <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
                      <prop k="outline_width_unit" v="MM"/>
                      <prop k="size" v="1.8"/>
                      <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
                      <prop k="size_unit" v="MM"/>
                      <prop k="vertical_anchor_point" v="1"/>
                    </layer>
                  </symbol>
                </layer>
              </symbol>
            </layer>
            <layer pass="0" class="FontMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="char_dd_active" v="1"/>
              <prop k="char_dd_expression" v="'Y = ' || round(x(&#xd;&#xa;&#x9;transform(point_n($geometry, @geometry_part_num), 'EPSG:4326',  @flts_source_crs )&#xd;&#xa;&#x9;), &#xd;&#xa;&#x9;3&#xd;&#xa;)"/>
              <prop k="char_dd_field" v=""/>
              <prop k="char_dd_useexpr" v="1"/>
              <prop k="chr" v="A"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="font" v="Arial"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="miter"/>
              <prop k="offset" v="-2,-1"/>
              <prop k="offset_dd_active" v="1"/>
              <prop k="offset_dd_expression" v="CASE WHEN degrees(&#xd;&#xa;&#x9;azimuth(centroid($geometry), point_n($geometry, @geometry_part_num))&#xd;&#xa;&#x9;) &lt; 90 THEN '6.0000, -7.0000'&#xd;&#xa;&#x9;WHEN degrees(&#xd;&#xa;&#x9;azimuth(centroid($geometry), point_n($geometry, @geometry_part_num))&#xd;&#xa;&#x9;) &lt; 180 THEN '6.0000, 4.0000'&#xd;&#xa;&#x9;WHEN degrees(&#xd;&#xa;&#x9;azimuth(centroid($geometry), point_n($geometry, @geometry_part_num))&#xd;&#xa;&#x9;) &lt; 270 THEN '-5.8000, 4.0000'&#xd;&#xa;ELSE&#xd;&#xa;&#x9;'-5.8000, -7.0000'&#xd;&#xa;END"/>
              <prop k="offset_dd_field" v=""/>
              <prop k="offset_dd_useexpr" v="1"/>
              <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="0,0,0,255"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="1.8"/>
              <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
              <effect enabled="1" type="effectStack">
                <effect type="dropShadow">
                  <prop k="blend_mode" v="13"/>
                  <prop k="blur_level" v="10"/>
                  <prop k="color" v="0,0,0,255"/>
                  <prop k="draw_mode" v="2"/>
                  <prop k="enabled" v="0"/>
                  <prop k="offset_angle" v="135"/>
                  <prop k="offset_distance" v="2"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="offset_unit_scale" v="0,0,0,0,0,0"/>
                  <prop k="transparency" v="0"/>
                </effect>
                <effect type="outerGlow">
                  <prop k="blend_mode" v="0"/>
                  <prop k="blur_level" v="1"/>
                  <prop k="color1" v="0,0,255,255"/>
                  <prop k="color2" v="0,255,0,255"/>
                  <prop k="color_type" v="0"/>
                  <prop k="discrete" v="0"/>
                  <prop k="draw_mode" v="2"/>
                  <prop k="enabled" v="1"/>
                  <prop k="single_color" v="255,255,255,255"/>
                  <prop k="spread" v="1"/>
                  <prop k="spread_unit" v="MM"/>
                  <prop k="spread_unit_scale" v="0,0,0,0,0,0"/>
                  <prop k="transparency" v="0"/>
                </effect>
                <effect type="drawSource">
                  <prop k="blend_mode" v="0"/>
                  <prop k="draw_mode" v="2"/>
                  <prop k="enabled" v="1"/>
                  <prop k="transparency" v="0"/>
                </effect>
                <effect type="innerShadow">
                  <prop k="blend_mode" v="13"/>
                  <prop k="blur_level" v="10"/>
                  <prop k="color" v="0,0,0,255"/>
                  <prop k="draw_mode" v="2"/>
                  <prop k="enabled" v="0"/>
                  <prop k="offset_angle" v="135"/>
                  <prop k="offset_distance" v="2"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="offset_unit_scale" v="0,0,0,0,0,0"/>
                  <prop k="transparency" v="0"/>
                </effect>
                <effect type="innerGlow">
                  <prop k="blend_mode" v="0"/>
                  <prop k="blur_level" v="3"/>
                  <prop k="color1" v="0,0,255,255"/>
                  <prop k="color2" v="0,255,0,255"/>
                  <prop k="color_type" v="0"/>
                  <prop k="discrete" v="0"/>
                  <prop k="draw_mode" v="2"/>
                  <prop k="enabled" v="0"/>
                  <prop k="single_color" v="255,255,255,255"/>
                  <prop k="spread" v="2"/>
                  <prop k="spread_unit" v="MM"/>
                  <prop k="spread_unit_scale" v="0,0,0,0,0,0"/>
                  <prop k="transparency" v="0.5"/>
                </effect>
              </effect>
            </layer>
            <layer pass="0" class="FontMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="char_dd_active" v="1"/>
              <prop k="char_dd_expression" v="'X = ' || round(y(&#xd;&#xa;&#x9;transform(point_n($geometry, @geometry_part_num), 'EPSG:4326',  @flts_source_crs )&#xd;&#xa;&#x9;), &#xd;&#xa;&#x9;3&#xd;&#xa;)"/>
              <prop k="char_dd_field" v=""/>
              <prop k="char_dd_useexpr" v="1"/>
              <prop k="chr" v="A"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="font" v="Arial"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="offset" v="-2,-1"/>
              <prop k="offset_dd_active" v="1"/>
              <prop k="offset_dd_expression" v="CASE WHEN degrees(&#xd;&#xa;&#x9;azimuth(centroid($geometry), point_n($geometry, @geometry_part_num))&#xd;&#xa;&#x9;) &lt; 90 THEN '6.5000, -4.8000'&#xd;&#xa;&#x9;WHEN degrees(&#xd;&#xa;&#x9;azimuth(centroid($geometry), point_n($geometry, @geometry_part_num))&#xd;&#xa;&#x9;) &lt; 180 THEN '6.3000, 6.2000'&#xd;&#xa;&#x9;WHEN degrees(&#xd;&#xa;&#x9;azimuth(centroid($geometry), point_n($geometry, @geometry_part_num))&#xd;&#xa;&#x9;) &lt; 270 THEN '-5.2000, 6.2000'&#xd;&#xa;ELSE&#xd;&#xa;&#x9;'-5.0000, -4.3000'&#xd;&#xa;END"/>
              <prop k="offset_dd_field" v=""/>
              <prop k="offset_dd_useexpr" v="1"/>
              <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="166,206,227,255"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="1.8"/>
              <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
              <effect enabled="1" type="effectStack">
                <effect type="dropShadow">
                  <prop k="blend_mode" v="13"/>
                  <prop k="blur_level" v="10"/>
                  <prop k="color" v="0,0,0,255"/>
                  <prop k="draw_mode" v="2"/>
                  <prop k="enabled" v="0"/>
                  <prop k="offset_angle" v="135"/>
                  <prop k="offset_distance" v="2"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="offset_unit_scale" v="0,0,0,0,0,0"/>
                  <prop k="transparency" v="0"/>
                </effect>
                <effect type="outerGlow">
                  <prop k="blend_mode" v="0"/>
                  <prop k="blur_level" v="1"/>
                  <prop k="color1" v="255,255,255,255"/>
                  <prop k="color2" v="207,209,213,255"/>
                  <prop k="color_type" v="0"/>
                  <prop k="discrete" v="0"/>
                  <prop k="draw_mode" v="2"/>
                  <prop k="enabled" v="1"/>
                  <prop k="single_color" v="255,255,255,255"/>
                  <prop k="spread" v="1"/>
                  <prop k="spread_unit" v="MM"/>
                  <prop k="spread_unit_scale" v="0,0,0,0,0,0"/>
                  <prop k="transparency" v="0"/>
                </effect>
                <effect type="drawSource">
                  <prop k="blend_mode" v="0"/>
                  <prop k="draw_mode" v="2"/>
                  <prop k="enabled" v="1"/>
                  <prop k="transparency" v="0"/>
                </effect>
                <effect type="innerShadow">
                  <prop k="blend_mode" v="13"/>
                  <prop k="blur_level" v="10"/>
                  <prop k="color" v="0,0,0,255"/>
                  <prop k="draw_mode" v="2"/>
                  <prop k="enabled" v="0"/>
                  <prop k="offset_angle" v="135"/>
                  <prop k="offset_distance" v="2"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="offset_unit_scale" v="0,0,0,0,0,0"/>
                  <prop k="transparency" v="0"/>
                </effect>
                <effect type="innerGlow">
                  <prop k="blend_mode" v="0"/>
                  <prop k="blur_level" v="3"/>
                  <prop k="color1" v="0,0,255,255"/>
                  <prop k="color2" v="0,255,0,255"/>
                  <prop k="color_type" v="0"/>
                  <prop k="discrete" v="0"/>
                  <prop k="draw_mode" v="2"/>
                  <prop k="enabled" v="0"/>
                  <prop k="single_color" v="255,255,255,255"/>
                  <prop k="spread" v="2"/>
                  <prop k="spread_unit" v="MM"/>
                  <prop k="spread_unit_scale" v="0,0,0,0,0,0"/>
                  <prop k="transparency" v="0.5"/>
                </effect>
              </effect>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale scalemethod="diameter"/>
  </renderer-v2>
  <labeling type="simple"/>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="labeling" value="pal"/>
    <property key="labeling/addDirectionSymbol" value="false"/>
    <property key="labeling/angleOffset" value="0"/>
    <property key="labeling/blendMode" value="0"/>
    <property key="labeling/bufferBlendMode" value="0"/>
    <property key="labeling/bufferColorA" value="255"/>
    <property key="labeling/bufferColorB" value="255"/>
    <property key="labeling/bufferColorG" value="255"/>
    <property key="labeling/bufferColorR" value="255"/>
    <property key="labeling/bufferDraw" value="false"/>
    <property key="labeling/bufferJoinStyle" value="128"/>
    <property key="labeling/bufferNoFill" value="false"/>
    <property key="labeling/bufferSize" value="1"/>
    <property key="labeling/bufferSizeInMapUnits" value="false"/>
    <property key="labeling/bufferSizeMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/bufferTransp" value="0"/>
    <property key="labeling/centroidInside" value="false"/>
    <property key="labeling/centroidWhole" value="true"/>
    <property key="labeling/decimals" value="3"/>
    <property key="labeling/displayAll" value="false"/>
    <property key="labeling/dist" value="0"/>
    <property key="labeling/distInMapUnits" value="false"/>
    <property key="labeling/distMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/drawLabels" value="false"/>
    <property key="labeling/enabled" value="false"/>
    <property key="labeling/fieldName" value=""/>
    <property key="labeling/fitInPolygonOnly" value="false"/>
    <property key="labeling/fontCapitals" value="0"/>
    <property key="labeling/fontFamily" value="MS Shell Dlg 2"/>
    <property key="labeling/fontItalic" value="false"/>
    <property key="labeling/fontLetterSpacing" value="0"/>
    <property key="labeling/fontLimitPixelSize" value="false"/>
    <property key="labeling/fontMaxPixelSize" value="10000"/>
    <property key="labeling/fontMinPixelSize" value="3"/>
    <property key="labeling/fontSize" value="8.25"/>
    <property key="labeling/fontSizeInMapUnits" value="false"/>
    <property key="labeling/fontSizeMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/fontStrikeout" value="false"/>
    <property key="labeling/fontUnderline" value="false"/>
    <property key="labeling/fontWeight" value="50"/>
    <property key="labeling/fontWordSpacing" value="0"/>
    <property key="labeling/formatNumbers" value="false"/>
    <property key="labeling/isExpression" value="true"/>
    <property key="labeling/labelOffsetInMapUnits" value="true"/>
    <property key="labeling/labelOffsetMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/labelPerPart" value="false"/>
    <property key="labeling/leftDirectionSymbol" value="&lt;"/>
    <property key="labeling/limitNumLabels" value="false"/>
    <property key="labeling/maxCurvedCharAngleIn" value="25"/>
    <property key="labeling/maxCurvedCharAngleOut" value="-25"/>
    <property key="labeling/maxNumLabels" value="2000"/>
    <property key="labeling/mergeLines" value="false"/>
    <property key="labeling/minFeatureSize" value="0"/>
    <property key="labeling/multilineAlign" value="4294967295"/>
    <property key="labeling/multilineHeight" value="1"/>
    <property key="labeling/namedStyle" value="Normal"/>
    <property key="labeling/obstacle" value="true"/>
    <property key="labeling/obstacleFactor" value="1"/>
    <property key="labeling/obstacleType" value="0"/>
    <property key="labeling/offsetType" value="0"/>
    <property key="labeling/placeDirectionSymbol" value="0"/>
    <property key="labeling/placement" value="1"/>
    <property key="labeling/placementFlags" value="10"/>
    <property key="labeling/plussign" value="false"/>
    <property key="labeling/predefinedPositionOrder" value="TR,TL,BR,BL,R,L,TSR,BSR"/>
    <property key="labeling/preserveRotation" value="true"/>
    <property key="labeling/previewBkgrdColor" value="#ffffff"/>
    <property key="labeling/priority" value="5"/>
    <property key="labeling/quadOffset" value="4"/>
    <property key="labeling/repeatDistance" value="0"/>
    <property key="labeling/repeatDistanceMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/repeatDistanceUnit" value="1"/>
    <property key="labeling/reverseDirectionSymbol" value="false"/>
    <property key="labeling/rightDirectionSymbol" value=">"/>
    <property key="labeling/scaleMax" value="10000000"/>
    <property key="labeling/scaleMin" value="1"/>
    <property key="labeling/scaleVisibility" value="false"/>
    <property key="labeling/shadowBlendMode" value="6"/>
    <property key="labeling/shadowColorB" value="0"/>
    <property key="labeling/shadowColorG" value="0"/>
    <property key="labeling/shadowColorR" value="0"/>
    <property key="labeling/shadowDraw" value="false"/>
    <property key="labeling/shadowOffsetAngle" value="135"/>
    <property key="labeling/shadowOffsetDist" value="1"/>
    <property key="labeling/shadowOffsetGlobal" value="true"/>
    <property key="labeling/shadowOffsetMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shadowOffsetUnits" value="1"/>
    <property key="labeling/shadowRadius" value="1.5"/>
    <property key="labeling/shadowRadiusAlphaOnly" value="false"/>
    <property key="labeling/shadowRadiusMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shadowRadiusUnits" value="1"/>
    <property key="labeling/shadowScale" value="100"/>
    <property key="labeling/shadowTransparency" value="30"/>
    <property key="labeling/shadowUnder" value="0"/>
    <property key="labeling/shapeBlendMode" value="0"/>
    <property key="labeling/shapeBorderColorA" value="255"/>
    <property key="labeling/shapeBorderColorB" value="128"/>
    <property key="labeling/shapeBorderColorG" value="128"/>
    <property key="labeling/shapeBorderColorR" value="128"/>
    <property key="labeling/shapeBorderWidth" value="0"/>
    <property key="labeling/shapeBorderWidthMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeBorderWidthUnits" value="1"/>
    <property key="labeling/shapeDraw" value="false"/>
    <property key="labeling/shapeFillColorA" value="255"/>
    <property key="labeling/shapeFillColorB" value="255"/>
    <property key="labeling/shapeFillColorG" value="255"/>
    <property key="labeling/shapeFillColorR" value="255"/>
    <property key="labeling/shapeJoinStyle" value="64"/>
    <property key="labeling/shapeOffsetMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeOffsetUnits" value="1"/>
    <property key="labeling/shapeOffsetX" value="0"/>
    <property key="labeling/shapeOffsetY" value="0"/>
    <property key="labeling/shapeRadiiMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeRadiiUnits" value="1"/>
    <property key="labeling/shapeRadiiX" value="0"/>
    <property key="labeling/shapeRadiiY" value="0"/>
    <property key="labeling/shapeRotation" value="0"/>
    <property key="labeling/shapeRotationType" value="0"/>
    <property key="labeling/shapeSVGFile" value=""/>
    <property key="labeling/shapeSizeMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeSizeType" value="0"/>
    <property key="labeling/shapeSizeUnits" value="1"/>
    <property key="labeling/shapeSizeX" value="0"/>
    <property key="labeling/shapeSizeY" value="0"/>
    <property key="labeling/shapeTransparency" value="0"/>
    <property key="labeling/shapeType" value="0"/>
    <property key="labeling/substitutions" value="&lt;substitutions/>"/>
    <property key="labeling/textColorA" value="255"/>
    <property key="labeling/textColorB" value="0"/>
    <property key="labeling/textColorG" value="0"/>
    <property key="labeling/textColorR" value="0"/>
    <property key="labeling/textTransp" value="0"/>
    <property key="labeling/upsidedownLabels" value="0"/>
    <property key="labeling/useSubstitutions" value="false"/>
    <property key="labeling/wrapChar" value=""/>
    <property key="labeling/xOffset" value="0"/>
    <property key="labeling/yOffset" value="0"/>
    <property key="labeling/zIndex" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerTransparency>0</layerTransparency>
  <displayfield>id</displayfield>
  <label>0</label>
  <labelattributes>
    <label fieldname="" text="Label"/>
    <family fieldname="" name="MS Shell Dlg 2"/>
    <size fieldname="" units="pt" value="12"/>
    <bold fieldname="" on="0"/>
    <italic fieldname="" on="0"/>
    <underline fieldname="" on="0"/>
    <strikeout fieldname="" on="0"/>
    <color fieldname="" red="0" blue="0" green="0"/>
    <x fieldname=""/>
    <y fieldname=""/>
    <offset x="0" y="0" units="pt" yfieldname="" xfieldname=""/>
    <angle fieldname="" value="0" auto="0"/>
    <alignment fieldname="" value="center"/>
    <buffercolor fieldname="" red="255" blue="255" green="255"/>
    <buffersize fieldname="" units="pt" value="1"/>
    <bufferenabled fieldname="" on=""/>
    <multilineenabled fieldname="" on=""/>
    <selectedonly on=""/>
  </labelattributes>
  <SingleCategoryDiagramRenderer diagramType="Histogram" sizeLegend="0" attributeLegend="1">
    <DiagramCategory penColor="#000000" labelPlacementMethod="XHeight" penWidth="0" diagramOrientation="Up" sizeScale="0,0,0,0,0,0" minimumSize="0" barWidth="5" penAlpha="255" maxScaleDenominator="1e+08" backgroundColor="#ffffff" transparency="0" width="15" scaleDependency="Area" backgroundAlpha="255" angleOffset="1440" scaleBasedVisibility="0" enabled="0" height="15" lineSizeScale="0,0,0,0,0,0" sizeType="MM" lineSizeType="MM" minScaleDenominator="inf">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute field="" color="#000000" label=""/>
    </DiagramCategory>
    <symbol alpha="1" clip_to_extent="1" type="marker" name="sizeSymbol">
      <layer pass="0" class="SimpleMarker" locked="0">
        <prop k="angle" v="0"/>
        <prop k="color" v="255,0,0,255"/>
        <prop k="horizontal_anchor_point" v="1"/>
        <prop k="joinstyle" v="bevel"/>
        <prop k="name" v="circle"/>
        <prop k="offset" v="0,0"/>
        <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
        <prop k="offset_unit" v="MM"/>
        <prop k="outline_color" v="0,0,0,255"/>
        <prop k="outline_style" v="solid"/>
        <prop k="outline_width" v="0"/>
        <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
        <prop k="outline_width_unit" v="MM"/>
        <prop k="scale_method" v="diameter"/>
        <prop k="size" v="2"/>
        <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
        <prop k="size_unit" v="MM"/>
        <prop k="vertical_anchor_point" v="1"/>
      </layer>
    </symbol>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings yPosColumn="-1" showColumn="-1" linePlacementFlags="10" placement="0" dist="0" xPosColumn="-1" priority="0" obstacle="0" zIndex="0" showAll="1"/>
  <annotationform>.</annotationform>
  <aliases>
    <alias field="id" index="0" name=""/>
    <alias field="upi" index="1" name=""/>
    <alias field="use" index="2" name=""/>
    <alias field="plot_numbe" index="3" name=""/>
    <alias field="area" index="4" name=""/>
    <alias field="scheme_id" index="5" name=""/>
    <alias field="crs_id" index="6" name=""/>
    <alias field="scheme_fie" index="7" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <attributeactions default="-1"/>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column width="-1" hidden="1" type="actions"/>
      <column width="-1" hidden="0" type="field" name="id"/>
      <column width="-1" hidden="0" type="field" name="upi"/>
      <column width="-1" hidden="0" type="field" name="use"/>
      <column width="-1" hidden="0" type="field" name="plot_numbe"/>
      <column width="-1" hidden="0" type="field" name="area"/>
      <column width="-1" hidden="0" type="field" name="scheme_id"/>
      <column width="-1" hidden="0" type="field" name="crs_id"/>
      <column width="-1" hidden="0" type="field" name="scheme_fie"/>
    </columns>
  </attributetableconfig>
  <editform>.</editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath>.</editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <widgets/>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <defaults>
    <default field="id" expression=""/>
    <default field="upi" expression=""/>
    <default field="use" expression=""/>
    <default field="plot_numbe" expression=""/>
    <default field="area" expression=""/>
    <default field="scheme_id" expression=""/>
    <default field="crs_id" expression=""/>
    <default field="scheme_fie" expression=""/>
  </defaults>
  <previewExpression></previewExpression>
  <layerGeometryType>2</layerGeometryType>
</qgis>
