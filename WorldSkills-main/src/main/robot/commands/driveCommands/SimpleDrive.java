package frc.robot.commands.driveCommands;

//WPI imports
import edu.wpi.first.wpilibj2.command.CommandBase;

//RobotContainer import
import frc.robot.RobotContainer;

//Subsystem imports
import frc.robot.subsystems.DriveBase;;

/**
 * SimpleDrive class
 * <p>
 * This class drives a motor at 50% speed until the command is ended
 */
public class SimpleDrive extends CommandBase
{
    //Grab the subsystem instance from RobotContainer
    private static final DriveBase driveBase = RobotContainer.driveBase;

    /**
     * Constructor
     */
    public SimpleDrive()
    {
        addRequirements(driveBase); // Adds the subsystem to the command
    }

    /**
     * Runs before execute
     */
    @Override
    public void initialize()
    {

    }

    /**
     * Called continously until command is ended
     */
    @Override
    public void execute()
    {
        driveBase.setDriverMotorSpeed(0.5, 0.5, 0.5); // Set motor speed to 50%
    }

    /**
     * Called when the command is told to end or is interrupted
     */
    @Override
    public void end(boolean interrupted)
    {
        driveBase.setDriverMotorSpeed(0.0, 0.0, 0.0); // Stop motor
    }

    /**
     * Creates an isFinished condition if needed
     */
    @Override
    public boolean isFinished()
    {
        return false;
    }

}