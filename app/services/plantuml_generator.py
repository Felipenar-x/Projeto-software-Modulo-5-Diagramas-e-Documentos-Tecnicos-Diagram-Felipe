def generate_plantuml(classes):
    lines = ["@startuml"]

    for cls in classes:
        lines.append(f"class {cls.name} {{")

        for attr in cls.attributes:
            lines.append(f"  {attr}")

        for method in cls.methods:
            lines.append(f"  {method}()")

        lines.append("}")

    lines.append("@enduml")

    return "\n".join(lines)