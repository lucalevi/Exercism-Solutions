// @ts-check

/**
 * Implement the classes etc. that are needed to solve the
 * exercise in this file. Do not forget to export the entities
 * you defined so they are available for the tests.
 */

// 1. Define Size for storing the dimensions of the window
export function Size(width = 80, height = 60) {
    this.width = width;
    this.height = height;

    this.resize = function (newWidth, newHeight) {
        this.width = newWidth;
        this.height = newHeight;
    };
}

// 2. Define Position to store a window position
export function Position(x = 0, y = 0) {
    this.x = x;
    this.y = y;

    this.move = function (newX, newY) {
        this.x = newX;
        this.y = newY;
    };
}

// 3. Define a ProgramWindow class
export class ProgramWindow {
    constructor() {
        this.screenSize = new Size(800, 600);
        this.size = new Size();
        this.position = new Position();
    }

    resize(newSize) {
        // Handle when input is an object
        const width = typeof newSize === 'object' ? newSize.width : newSize;
        const height = typeof newSize === 'object' ? newSize.height : arguments[1];

        // Ensure width and height are at least 1
        const constrainedWidth = Math.max(1, width);
        const constrainedHeight = Math.max(1, height);

        // Ensure window doesn't exceed screen bounds considering position
        const maxWidth = this.screenSize.width - this.position.x;
        const maxHeight = this.screenSize.height - this.position.y;

        // Apply the constrained values
        this.size.resize(
            Math.min(constrainedWidth, maxWidth),
            Math.min(constrainedHeight, maxHeight)
        );
    }

    move(newPosition) {
        // Handle when input is an object
        const newX = typeof newPosition === 'object' ? newPosition.x : newPosition;
        const newY = typeof newPosition === 'object' ? newPosition.y : arguments[1];

        // Ensure position is not negative
        const x = Math.max(0, newX);
        const y = Math.max(0, newY);

        // Ensure window stays within screen bounds considering size
        const maxX = this.screenSize.width - this.size.width;
        const maxY = this.screenSize.height - this.size.height;

        // Apply the constrained values
        this.position.move(
            Math.min(x, maxX),
            Math.min(y, maxY)
        );
    }
}

// 6. Change a program window
export function changeWindow(programWindow) {
    programWindow.resize(400, 300);
    programWindow.move(100, 150);
    return programWindow;
}
