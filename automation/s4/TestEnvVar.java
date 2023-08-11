public class TestEnvVar {
	public static void main(String[] args) {
		String myVar = System.getenv().get("PATH");
		System.out.println(myVar);
		String mySecondVar = System.getenv().get("HEY");
		mySecondVar = mySecondVar != null ? mySecondVar : "La variable no existe";
		System.out.println(mySecondVar);
	}
}
