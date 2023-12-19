from detector import collect_builders

test_input_path1 = "./prj1/"
test_input_path2 = "./prj2/"

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
            }
    }

    result = collect_builders(test_input_path2)
    assert expected == result
