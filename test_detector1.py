from detector import collect_builders

test_input_path1 = "./prj1/"
test_input_path2 = "./prj2/"
test_input_path3 = "./centrifuge-java"
test_input_path4 = "./JavaOSC";
test_input_path5 = "./virtutiCebulari"

def test_detector1():
    expected = {
        "ComputerBuilder":
            { "builder_methods": {"setGraphicCard", "setSpeaker"},
              "build_methods": {"build"}
            }
    }

    result = collect_builders(test_input_path1)
    assert expected == result

def test_detector2():
    expected = {
        "Builder":
            { "builder_methods": {"age", "name", "nationality", "skinColor"},
              "build_methods": {"build"}
            },
        "WolverineBuilder":
            { "builder_methods": {"buildXFactor", "buildLover"},
              "build_methods": {"buildXman", "buildYman"}
            },
        "XMan":
            { "builder_methods": {"setxFactor", "setLover"},
              "build_methods": {"getxFactor", "getLover"}
            }
    }

    result = collect_builders(test_input_path2)
    assert expected == result

def test_detector3():
    expected = {'Builder': {'builder_methods': {'withReverse', 'withLimit', 'withSince'}, 'build_methods': {'build'}}}
    result = collect_builders(test_input_path3)
    assert expected == result

def test_detector4():
    expected = {'OSCSerializerAndParserBuilder': {'builder_methods': {'unregisterArgumentHandler', 'setProperties', 'addProperties', 'clearProperties', 'setUsingDefaultHandlers', 'registerArgumentHandler'}, 'build_methods': {'getIdentifierToTypeMapping', 'getProperties', 'buildParser', 'clearProperties'}}, 'OSCPortInBuilder': {'builder_methods': {'addMessageListener', 'setPacketListeners', 'setLocalPort', 'setLocalSocketAddress', 'setPort', 'setPacketListener', 'setRemoteSocketAddress', 'setNetworkProtocol', 'setSocketAddress', 'setRemotePort', 'addPacketListener'}, 'build_methods': {'build', 'addDefaultPacketListener'}}, 'OSCPortOutBuilder': {'builder_methods': {'setLocalPort', 'setLocalSocketAddress', 'setPort', 'setRemoteSocketAddress', 'setNetworkProtocol', 'setSocketAddress', 'setRemotePort'}, 'build_methods': {'build'}}, 'OSCTimeTag64': {'builder_methods': {'clone', 'valueOf'}, 'build_methods': {'toString', 'isImmediate', 'getFraction', 'toInstant', 'clone', 'getSeconds', 'getNtpTime', 'toDate', 'immediateDate', 'getNanos', 'hashCode'}}, 'OSCSymbol': {'builder_methods': {'clone', 'valueOf'}, 'build_methods': {'clone', 'hashCode', 'toString'}}, 'OSCMidiMessage': {'builder_methods': {'clone', 'valueOf'}, 'build_methods': {'getPortId', 'toContentArray', 'clone', 'getData2', 'getData1', 'getStatus', 'hashCode'}}, 'OSCColor': {'builder_methods': {'clone', 'valueOf'}, 'build_methods': {'getAlpha', 'getAlphaInt', 'getRedInt', 'toContentArray', 'clone', 'getBlueInt', 'getBlue', 'getGreenInt', 'getRed', 'getGreen', 'hashCode'}}, 'OSCUnsigned': {'builder_methods': {'clone', 'valueOf'}, 'build_methods': {'toString', 'clone', 'hashCode', 'toLong'}}}
    result = collect_builders(test_input_path4)
    assert sorted(expected) == sorted(result)

def test_detector5():
    expected = {'ProductDTOBuilder': {'builder_methods': {'aProductDTO', 'withAmount', 'withNewPrice', 'withProductUrl', 'withProductName', 'withShop', 'withOldPrice', 'withPictureUrl', 'withShopName', 'withId'}, 'build_methods': {'aProductDTO', 'build'}}}
    result = collect_builders(test_input_path5)
    assert sorted(expected) == sorted(result)
