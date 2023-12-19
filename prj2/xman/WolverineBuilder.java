package create.builder;

/**
 * 金刚狼的builder
 * @author Chayne_Shen 2017/3/10 0010.
 */

public class WolverineBuilder implements XManBuilder {
    XMan mXMan;
    WolverineBuilder() {
        mXMan = new XMan();
    }

    public WolverineBuilder buildXFactor(String factor) {
        mXMan.setxFactor(factor);
        System.out.println(mXMan.getxFactor());
        return this;
    }

    public WolverineBuilder buildLover(String lover) {
        mXMan.setLover(lover);
        System.out.println(mXMan.getLover());
        return this;
    }

    public XMan buildXman() {
        System.out.println("Wolverine is successfully built");

        return mXMan;
    }

    public XMan buildYman() {
        System.out.println("Wolverine is successfully built");

        return mXMan;
    }
}
